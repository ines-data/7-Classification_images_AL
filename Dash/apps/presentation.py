from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
from dash_core_components.Markdown import Markdown
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app, server
import os
from skimage.io import imread
from apps import data, prediction, classification


text = """  
- Identifier à quelle catégorie appartient un objet  
- La classification est un type d'apprentissage automatique """
text1 = """ 
- Solution automatisée
- Gain de temps et d'énérgie
"""
text2 = """ 
-  L'imagerie médicale 
-  Reconnaissance d'objets dans des images
-  Reconnaissance faciale
-  Détectez les chiffres écrits à la main
-  Apprendre une langue aux enfants
"""
text3 = """
-  Machine Learning (SVM, arbres de décision, KNN, ... )
-  Deep learning ("CNN")
"""
layout = html.Div([
        dbc.Container([
                html.H1("Classification d'images", style={'textAlign':'center'},className="mb-4 mt-4"),
                dbc.Row([
                dbc.Col(html.Img(src="/assets/animaux.jpeg", height="150px")
                        , className="mb-4 text-center")
                ]),
     dcc.Markdown(text, style={'font-size':'20px'}, className="mb-4 mt-4"),
#     html.H4('Atouts :', className="mb-4 mt-4"),
#     dcc.Markdown(text1, style={'font-size':'20px'}),
#     html.H4("Exemples d'utilisation:"),
#     dcc.Markdown(text2, style={'font-size':'20px'}),
#     html.H4('Modèles :'),
#     dcc.Markdown(text3, style={'font-size':'20px'}),
    dbc.Row([html.H1("")]),
    dbc.Row([
            dbc.Col(dbc.Card(children=[html.H2(children='Atouts : ',className="text-center"),
                                        dcc.Markdown(text1, style={'font-size':'20px'})],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H2(children='Exemples : ',className="text-center"),
                                        dcc.Markdown(text2, style={'font-size':'20px'})],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H2(children='Modèles :',
                                               className="text-center"),
                                        dcc.Markdown(text3, style={'font-size':'20px'})


                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),
            
        ], className="mb-5")
])
])