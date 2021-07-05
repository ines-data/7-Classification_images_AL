from dash_bootstrap_components._components.Row import Row
from dash_core_components.Markdown import Markdown
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash_html_components.Div import Div
from dash_html_components.H2 import H2
from dash_html_components.H3 import H3
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
from apps import data, presentation, classification
from joblib import dump, load



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


layout = html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col(html.H1("Prédiction", className="text-center")
                        , className="mb-4 mt-4")
            ]),
            dbc.Row([
                dbc.Col(html.Img(src="/assets/animaux.jpeg", height="150px")
                        , className="mb-4 text-center")
                ]),
            
            html.Div([
                dbc.Row([
                #dbc.Col(html.H5(style={'color': '#585858'}, children="Vous pouvez télécharger une image d'animal afin d'obtenir son nom :")                        )#, className="mb-4")
                ]),
            dcc.Upload(
            id='upload-image',
            children=html.Div([
                #'Séléctioner une image',
                html.A('Selectioner une image')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'solid',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px',
                'background-color':'#81BEF7'
            },
            # Allow multiple files to be uploaded
            multiple=True
            ),
            html.Div(id='output-image-upload', style = {'textAlign': 'center', 'font-size': '200px'}, className="mb-4"),
            html.Div(id='prediction',style={'textAlign': 'center', 'color':'#424242', 'font-size': '50px'}),
                html.A("Vous pouvez obtenir le code complet de l'application sur mon référentiel github"
                , style = {'textAlign': 'left', 'font-size': '15px'}
                , href="https://github.com/ines-data/")
            ])
            
        ])
        
])

        
def parse_contents(contents):
    
    return html.Img(src=contents, style={'height':'200px', 'width':'200px'})


#callback classification 
@app.callback([Output('output-image-upload', 'children'), Output('prediction', 'children')],
              [Input('upload-image', 'contents')])


def update_output(image):        
    
    if image is not None:
       
        children = parse_contents(image[0]) 
        img_data = image[0]
        img_data = re.sub('data:image/jpeg;base64,', '', img_data)
        img_data = base64.b64decode(img_data)  
        
        stream = io.BytesIO(img_data)
        img_pil = Image.open(stream)
        
        
        #Load model, change image to array and predict
        model = load_model('model2_augmentation_data.h5')


        dim = (150, 150)
        
        img = np.array(img_pil.resize(dim))
        
        x = img.reshape(1,150,150,3)

        answ = model.predict(x)
        classification = np.where(answ == np.amax(answ))[1][0]
        
        pred = names(classification)   
        
                 
        return  children, pred
        
    else:
        return (no_update, no_update) 