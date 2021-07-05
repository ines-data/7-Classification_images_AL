from dash_bootstrap_components._components.Row import Row
from dash_core_components.Markdown import Markdown
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash_html_components.Div import Div
#from dash_html_components.H3 import H3
from app import app, server
import datetime
from skimage.transform import resize
import pickle
from PIL import Image
import base64
import io
from io import BytesIO
import re
import numpy as np
from tensorflow import keras
import tensorflow as tf
from keras.models import load_model
from sklearn.preprocessing import OneHotEncoder
from dash import no_update
from apps import data, presentation, prediction
from joblib import dump, load
import pandas as pd

df = pd.DataFrame({'index':['Score'],'Machine learning(SGD)':[0.78], 'Deep learning(CNN)':[0.85]
                ,'Transfer learning':[0.91], 'Transfer learning + Augmentation Data':[0.95]}
                  , index=['Score'])#, 'Presicion', 'f1_score'])

text1 = """
- SVM (Support Vector Machines)  
- SGD 
"""
text2 = """
Réseau neuronal convolutif (CNN) qui repose sur l’application de filtres inspirés 
du fonctionnement de la partie du cerveau traitant du champ visuel
"""
text3 = """
Utiliser un modèle pré entraîné afin de réentraîner partiellement le modèle avec notre base de données
"""
text4 = """  
Augmenter la quantité de données en ajoutant des copies légèrement modifiées de données déjà existantes
"""

#classes = ["Bear","Duck","Eagle","Elephant","Lion","Rabbit","Sheep","Wolf"]
classes = ["Ours", "Canard", "Aigle", "Eléphant", "Lion", "Lapin", "Brebis", "Loup"]
enc = OneHotEncoder()
enc.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8]]) 
def names(number):
    if(number == 0):
        return 'Ours'
    elif(number == 1):
        return 'Canard'
    elif(number == 2):
        return 'Aigle'
    elif(number == 3):
        return 'Eléphant'
    elif(number == 4):
        return 'Lion'
    elif(number == 5):
        return 'Lapin'
    elif(number == 6):
        return 'Brebis'
    elif(number == 7):
        return 'Loup'


top_card1_1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/lion3.jpeg", top=True),
        dbc.CardBody(
            html.P("Brebis", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)

top_card1_2 = dbc.Card(
    [
       dbc.CardImg(src="/assets/elephant5.jpeg", top=True),
        dbc.CardBody(
            html.P("Ours", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)
top_card2_1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/lion3.jpeg", top=True),
        dbc.CardBody(
            html.P("Aigle", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)

top_card2_2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/elephant5.jpeg", top=True),
        dbc.CardBody(
            html.P("Lapin", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)
top_card3_1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/lion3.jpeg", top=True),
        dbc.CardBody(
            html.P("Lion", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)

top_card3_2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/elephant5.jpeg", top=True),
        dbc.CardBody(
            html.P("Canard", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)
top_card4_1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/lion3.jpeg", top=True),
        dbc.CardBody(
            html.P("Lion", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)

top_card4_2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/elephant5.jpeg", top=True),
        dbc.CardBody(
            html.P("Eléphant", style={'textAlign': 'center','font-size':'25px'}, className="card-text")
        ),
    ],
    style={"width": "18rem"},
)

layout = html.Div([
        dbc.Container([
            dbc.Row([dbc.Col(html.H1("Analyser et interpréter les données", className="text-center"), className="mb-4 mt-4")]),
            dbc.Row([
                dbc.Col(html.Img(src="/assets/animaux.jpeg", height="150px")
                        , className="mb-4 text-center")
                ]),
            html.Div([html.H2("Apprentissage automatique (Machine Learning) : ")], className="mb-4 mt-4"),
            html.Div([
                html.Div([
                    dbc.Row([
                        dbc.Col(dcc.Markdown(text1, style={'font-size':'25px'})),
                    ]),
                    dbc.Row([
                        dbc.Col(),dbc.Col(top_card1_1, width="auto"), dbc.Col(top_card1_2, width="auto"),dbc.Col(),
                        #dbc.Col(dcc.Markdown(text1, style={'font-size':'25px'})),
                    
                    ]),
            
            html.Div([html.H2("Apprentissage profond (Deep Learning) : ")], className="mb-4 mt-4"),
            html.Div([
                dbc.Row([
                        dbc.Col(dcc.Markdown(text2, style={'font-size':'25px'})),
                    ]),
                    dbc.Row([
                        dbc.Col(),dbc.Col(top_card2_1, width="auto"), dbc.Col(top_card2_2, width="auto"),dbc.Col(),
                        #dbc.Col(dcc.Markdown(text2, style={'font-size':'25px'})),
                    ])
            ]),
        html.Div([html.H2("Transfert de connaissances (transfer learning) : ")], className="mb-4 mt-4"),
        html.Div([
            dbc.Row([
                        dbc.Col(dcc.Markdown(text3, style={'font-size':'25px'})),
                    ]),
                    dbc.Row([
                        dbc.Col(),dbc.Col(top_card3_1, width="auto"), dbc.Col(top_card3_2, width="auto"),dbc.Col(),
                        #dbc.Col(dcc.Markdown(text3, style={'font-size':'25px'})),
                    ])
        ]),
        html.Div([html.H2("Transfert de connaissances + Augmentation de données : ")], className="mb-4 mt-4"),
        html.Div([
            dbc.Row([
                        dbc.Col(dcc.Markdown(text4, style={'font-size':'25px'})),
                    ]),
                    dbc.Row([
                        dbc.Col(),dbc.Col(top_card4_1, width="auto"), dbc.Col(top_card4_2, width="auto"),dbc.Col(),
                        #dbc.Col(dcc.Markdown(text4, style={'font-size':'25px'})),
                    ])
        ]),
        html.Div([html.H2("Tableau des Metrics")], className="mb-4 mt-4"),
        html.Div([
                dbc.Col(dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),className="card-text")
            ])
        
        ]),
        dbc.Row([
            html.Div(id='app-1-display-value'),
            dbc.Col(),dcc.Link('Haut de page', href='/classification')
        ]),
        html.A("Vous pouvez obtenir le code complet de l'application sur mon référentiel github"
                , style = {'textAlign': 'left', 'font-size': '15px'}
                , href="https://github.com/ines-data/")
            
            
        ])
        
])
])
