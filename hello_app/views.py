from datetime import datetime
from flask import Flask, render_template
from . import app


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

data = pd.read_csv('claim.csv')

names = list(data.columns)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1(
        children='Claims Assessor App',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='View Risk rating for each Feature', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div([
        dcc.Dropdown(
            id='ddl_x',
            options=[{'label': i, 'value': i} for i in names],
            value='sepal-width',
            style={'width':'50%'}
        )]),

    html.Div([
        dcc.Graph(id='graph1')
    ],style={'width':'100%','display':'inline-block'})


])



if __name__ == '__main__':
    app.run_server(port = 8000, debug = True)

