import mysql.connector
import pandas as pd

def carregar_dados():
    cnx = mysql.connector.connect(
        user="glpi-tecnocomp",
        password=password,
        host=hostname,
        database=database
    )
    cursor = cnx.cursor()

    query = """ 
        SELECT 
    t.id AS "id",
    t.name AS "titulo",
    t.content AS "descricao",
    -- Mapeamento do status do ticket
    CASE 
        WHEN t.status = 1 THEN 'Novo'
        WHEN t.status = 2 THEN 'Em atendimento'
        WHEN t.status = 3 THEN 'Atendimento Planejado'
        WHEN t.status = 4 THEN 'Pendente'
        WHEN t.status = 5 THEN 'Solucionado'
        WHEN t.status = 6 THEN 'Fechado'
        ELSE 'Desconhecido' -- Para casos inesperados
    END AS "status",
    t.date_creation AS "data_criacao",
    t.solvedate AS "data_solucao",
    t.date_mod AS "DATA DA ÚLTIMA MODIFICAÇÃO",
    -- Requerente
    MAX(CASE 
        WHEN tu.type = 1 THEN tu.users_id 
        ELSE NULL 
    END) AS "id_requerente",
    MAX(CASE 
        WHEN tu.type = 1 THEN CONCAT(u.firstname, ' ', u.realname) 
        ELSE NULL 
    END) AS "nome_requerente",
    MAX(CASE 
        WHEN tu.type = 1 THEN u.name 
        ELSE NULL 
    END) AS "email_requerente",
    -- Técnico
    MAX(CASE 
        WHEN tu.type = 2 THEN tu.users_id 
        ELSE NULL 
    END) AS "id_tecnico",
    MAX(CASE 
        WHEN tu.type = 2 THEN CONCAT(u.firstname, ' ', u.realname) 
        ELSE NULL 
    END) AS "nome_tecnico",
    MAX(CASE 
        WHEN tu.type = 2 THEN u.name 
        ELSE NULL 
    END) AS "email_tecnico",
     MAX(CASE 
        WHEN ggt.type = 2 THEN gg.name 
        ELSE NULL 
    END) AS "grupo_tecnico"
FROM 
    glpi_tickets t
LEFT JOIN 
    glpi_tickets_users tu ON t.id = tu.tickets_id
LEFT JOIN 
    glpi_users u ON tu.users_id = u.id
INNER JOIN 
    glpi_requesttypes rt ON t.requesttypes_id = rt.id
LEFT JOIN 
    glpi_itilcategories ic ON ic.id = t.itilcategories_id
LEFT JOIN 
	glpi_groups_tickets ggt ON GGT.tickets_id = t.id
LEFT JOIN
	glpi_groups gg ON gg.id = ggt.groups_id
GROUP BY 
    t.id, t.name,t.time_to_resolve, t.solvedate , rt.name, t.status,t.content , t.date_creation, t.date_mod, ic.completename;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    cursor.close()
    cnx.close()

    df['data_criacao'] = pd.to_datetime(df['data_criacao'])
    df['data_modificacao'] = pd.to_datetime(df['data_modificacao'])
    df['tempo_para_solucao'] = pd.to_datetime(df['tempo_para_solucao'])
    df['sla_estourado'] = df.apply(lambda row:
        "Não solucionado" if pd.isna(row['data_solucao']) else
        "Sim" if row['data_solucao'] > row['tempo_para_solucao'] else
        "Não", axis=1)
    df['data_abertura'] = df['data_criacao'].dt.strftime('%Y-%m-%d')
    df['hora_abertura'] = df['data_criacao'].dt.hour
    df['month'] = df['data_criacao'].dt.strftime('%Y-%m')
    return df
