
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = px.data.iris()

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Iris Data'),

    html.Label("Select flower species"),

    dcc.Dropdown(
        id="species_dropdown",
        options=[
            {'label': 'Setosa', 'value': 'setosa'},
            {'label': 'Versicolor', 'value': 'versicolor'},
            {'label': 'Virginica', 'value': 'virginica'}
        ],
        value='setosa',
        clearable=False
    ),

    dcc.Graph(id='iris_graph')
])


@app.callback(
    Output(component_id='iris_graph', component_property='figure'),
    Input(component_id='species_dropdown', component_property='value')
)
def update_graph(selected_species):
    filtered_df = df[df['species'] == selected_species]

    fig = px.scatter(
        filtered_df,
        x='sepal_width',
        y='sepal_length',
        color='species',
        title=f'Iris Data - {selected_species}'
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
