from dash import Dash, dcc, html, page_container, page_registry
import dash_bootstrap_components as dbc
from data.conexao import carregar_dados

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Store(id="global-data", data=carregar_dados().to_dict("records")),
    html.Div([
        html.H2("Dashboard GLPI - Tecnocomp", style={"padding": "20px"}),
        page_container
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
