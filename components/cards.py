from dash import html

def metric_card(title, value, color="#FF7100"):
    return html.Div([
        html.Div(title, className="metric-title", style={"color": color}),
        html.Div(value, className="metric-value", style={"color": color}),
    ], className="metric-card")
