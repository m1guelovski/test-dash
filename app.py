import os

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv")

app = Dash()

app.layout = [
    html.H1(children="Moritz exploring dash", style={"textAlign":"center"}),
    dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
    dcc.Graph(id="graph-content")
]

@callback(
    Output("graph-content", "figure"),
    Input("dropdown-selection", "value")
)
def update_graph(value):
    dff = df[df['country'] == value]
    fig = px.line(dff, x="year", y="pop", title=f"Population Over Time in {value}")
    fig.update_traces(hovertemplate='Year: %{x}<br>Population: %{y}')
    return fig

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use a porta definida na variável de ambiente PORT ou padrão 8000
    app.run_server(debug=False, host="0.0.0.0", port=port)

