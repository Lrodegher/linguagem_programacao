from dash import register_page, html, dcc, Input, Output, State, callback
import pandas as pd
from datetime import datetime
from components.cards import metric_card

register_page(__name__, path="/chamados-diarios")

def layout():
    return html.Div([
        dcc.Store(id="df-chamados-diarios"),
        html.H2("Página de Chamados Diários"),
        html.Div(id="cards-chamados-diarios", style={"display": "flex", "gap": "15px", "marginTop": "20px"}),
        html.Hr(),
        html.Div(id="tabela-chamados-diarios")
    ])

@callback(
    Output("df-chamados-diarios", "data"),
    Input("global-data", "data")
)
def preparar_dados(data):
    df = pd.DataFrame(data)
    df = df[df['status'].isin(["Em atendimento", "Novo", "Pendente"])]
    now = pd.Timestamp.now()
    df['data_modificacao'] = pd.to_datetime(df['data_modificacao'])
    df['tempo_para_solucao'] = pd.to_datetime(df['tempo_para_solucao'])

    df['desatualizado'] = df['data_modificacao'].apply(lambda x: "Sim" if (now - x).days > 1 else "Não")

    df['tempo_sla_estourar'] = df.apply(
        lambda x: round((x['tempo_para_solucao'] - now).total_seconds() / 3600, 2)
        if x['status'] == 'Em atendimento' else None,
        axis=1
    )

    df['sla_proximo_estourar'] = df.apply(
        lambda x: "Sem SLA" if pd.isna(x['tempo_sla_estourar']) else
                  "SLA estourado" if x['tempo_sla_estourar'] < 0 else
                  "Sim" if x['tempo_sla_estourar'] < 2 else
                  "Não",
        axis=1
    )

    return df.to_dict("records")

@callback(
    Output("cards-chamados-diarios", "children"),
    Input("df-chamados-diarios", "data")
)
def atualizar_cards(data):
    df = pd.DataFrame(data)

    pendente = df[df['status'] == "Pendente"].shape[0]
    atendimento = df[df['status'] == "Em atendimento"].shape[0]
    desatualizados = df[df['desatualizado'] == "Sim"].shape[0]
    sla_critico = df[df['sla_proximo_estourar'] == "Sim"].shape[0]

    def cor(valor, l1, l2):
        if valor >= l2: return "red"
        elif valor >= l1: return "orange"
        return "green"

    return [
        metric_card("Chamados Pendente", pendente, color=cor(pendente, 5, 10)),
        metric_card("Chamados em Atendimento", atendimento, color=cor(atendimento, 8, 15)),
        metric_card("Chamados Desatualizados", desatualizados),
        metric_card("SLA Próximo de Estourar", sla_critico)
    ]

@callback(
    Output("tabela-chamados-diarios", "children"),
    Input("df-chamados-diarios", "data")
)
def atualizar_tabela(data):
    df = pd.DataFrame(data)
    df_view = df[['id','status','Categoria','nome_requerente','nome_tecnico','grupo_tecnico','desatualizado','sla_proximo_estourar']]
    return dcc.Markdown("### Lista de Chamados") + dcc.Graph(
        figure= {
            "data": [
                {
                    "type": "table",
                    "header": {"values": list(df_view.columns)},
                    "cells": {"values": [df_view[col] for col in df_view.columns]}
                }
            ]
        }
    )
