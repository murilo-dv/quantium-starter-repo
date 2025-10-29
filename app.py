from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame(pd.read_csv('cleaned_data.csv',))

fig = px.line(df, x='date',y='sales', color='region', markers=True, title='Sales by Region Over Time')



app.layout = html.Div(style={'backgroundColor': colors['background']},
    children=[
        html.Div(children=html.H1(children='Soul Foods Report')),
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