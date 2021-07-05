
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash
from app import app, server
from apps import presentation, data, classification, prediction


server = app.server



dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Présentation", href="/presentation"),
        dbc.DropdownMenuItem("Données", href="/data"),
        dbc.DropdownMenuItem("Classification", href="/classification"),
        dbc.DropdownMenuItem("Prédiction", href="/prediction"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explorer",
)

navbar = dbc.NavbarSimple(
    brand="Classification d'images / Reconnaissance d'images",
    brand_href="#",
    color="primary",
    dark=True,
)

def get_menu():
    menu = html.Div(style={'font-size': '20px', 'background-color':'#EBF0F5', 'textAlign': 'center', 'color':'rgba(0,0,7,0.7)'}, children=[ 

        dcc.Link('Présentation  | ', href='/presentation', className="mb-3"),

        dcc.Link(' Données  | ', href='/data', className="mb-3"),

        dcc.Link(' Classification  | ', href='/classification', className='mb-3'),
        
        dcc.Link(' Prédiction  | ', href='/prediction', className='mb-3')

    ], className="rows")
    return menu


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    get_menu(),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/presentation':
        return presentation.layout
    if pathname == '/data':
        return data.layout
    if pathname == '/prediction':
        return prediction.layout
    if pathname == '/classification':
        return classification.layout
    else:
        return presentation.layout

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)