from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.DataFrame(pd.read_csv('cleaned_data.csv',))

fig = px.line(df, x='date',y='sales', color='region', markers=True)

app.layout = html.Div(
    children=[
        html.H1(children='Soul Foods Report'),
        html.Div(children='''
        Report of sales, sorted by date and filter by region.
    '''),
        dcc.Graph(
            id='Sales',
            figure=fig
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)