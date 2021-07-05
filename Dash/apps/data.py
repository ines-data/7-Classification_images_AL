import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app, server
import os
import numpy as np
from skimage.io import imread
from PIL import Image
from apps import presentation, prediction, classification
import random




layout = html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col(html.H1(children="Data", className="text-center"), className="mb-4 mt-4")
            ]),
                    dbc.Row([
                dbc.Col(html.H5(style={'color': "#585858"}, children='')                        
                        , className="mb-4")
                ]),
            dbc.Row([
                dbc.Col(dbc.Card(children=[html.H5(children='Ours',className="text-center"),
                                        html.Img(src="/assets/bear1.jpeg", height="100px")]),),
                dbc.Col(dbc.Card(children=[html.H5(children='Canard',className="text-center"),
                                        html.Img(src="/assets/duck1.jpeg", height="100px")]),),
                dbc.Col(dbc.Card(children=[html.H5(children='Aigle',className="text-center"),
                                        html.Img(src="/assets/eagle1.jpeg", height="100px")]),),
                dbc.Col(dbc.Card(children=[html.H5(children='Eléphant',className="text-center"),
                                        html.Img(src="/assets/elephant1.jpeg", height="100px")]),),
                dbc.Col(dbc.Card(children=[html.H5(children='Lion',className="text-center"),
                                        html.Img(src="/assets/lion1.jpeg", height="100px")]),),
                dbc.Col(dbc.Card(children=[html.H5(children='Lapin', className="text-center"),
                                        html.Img(src="/assets/rabbit01.jpeg", height="100px")]),),
                dbc.Col(dbc.Card(children=[html.H5(children='Brebis',className="text-center"),
                                        html.Img(src="/assets/sheep1.jpeg", height="100px")]),),
                dbc.Col(dbc.Card(children=[html.H5(children='Loup', className="text-center"),
                                        html.Img(src="/assets/wolf1.jpeg", height="100px")])
                        ,className="mb-4"),

            ]),
            dbc.Row([
                dbc.Col(dcc.Input(id="input1", type="text", placeholder="Tapez votre texte", debounce=True), className="mb-4 text-center")
            ]),
            dbc.Row([
                dbc.Col(html.H2(id="output"), className="mb-4 text-center")
            ]),
            html.A("Vous pouvez obtenir le code complet de l'application sur mon référentiel github",
                href="https://github.com/ines-data/")
            ], className="mb-5"), 
])



def generate_thumbnail(image):
    return html.Div([
            html.Img(
                src = image,
                style = {
                    'height': '180px',
                    'width': '180px',
                    'float': 'left',
                    'position': 'relative',
                    'padding-top': 15,
                    'padding-right': 15,

                }
            )
        ],className="text-center")

@app.callback(
    Output("output", "children"),
    Input("input1", "value"),)
def update_output(input1):  
    
    if input1 != None:
        text = input1.capitalize()
        for subdir in os.listdir(fr'/home/ines/Documents/CoursAnneLaure/7-Classification_image/Data2'):
            if text == subdir[:-4]:
                print(subdir)
                current_path = os.path.join(fr'/home/ines/Documents/CoursAnneLaure/7-Classification_image/Data2', subdir)

                images_div = []
                for file in os.listdir(current_path):
                        image = Image.open(current_path+"/"+file).convert('RGB')
                        images_div.append(generate_thumbnail(image))
                #return html.Div(np.random.choice(images_div, 12))
                l = len(images_div)
                return html.Div([l]), html.Div(images_div[0:12])
        else:
            return "NO"