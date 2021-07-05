#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:03:36 2021

@author: sacia
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from apps import home, page1, page0, prediction


colors = {
    #'background': '#111111',
    'text': '#7FDBFF'
}

# - Layout -

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(
                children='Classification de textes ',
                style={
                    'textAlign': 'center',
                    'color': colors['text']}),
                ) 
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Une tâche NPL (Natural Language Processing) '), className="mb-4")
        ]),
        
         dbc.Row([
            dbc.Col(html.H6(children='Mettre une étiquette sur un texte'), className="mb-4")
        ]),
         
        # Application 
        dbc.Row([
            dbc.Col(html.H4(
                   children='Applications :'),
                   
             
                style={
                    'textAlign': 'center',
                    'color': '#7FDBFF' }),

        ]),
        
        dbc.Row([
            dbc.Col(html.H6(children='Analyse de sentiments, Détection de spams , Détection de langue, Classification de documents... '), className="mb-4")
        ]),
      
        #modèle ML
        dbc.Row([
            dbc.Col(html.H4(children='Modèle de Machine Learning (ML):'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Entraînement  +  Inférence'), className="mb-2")
        ]),
        
        # Alog ML
        
         dbc.Row([
            dbc.Col(html.H4(children='Algorithmes de ML :'), className="mb-2")
        ]),
         
       dbc.Row([
            dbc.Col(html.H6(children='le SVM ( support vector machine), la Regression Logistique, le Random Forest, le K-Nearest Neighbors (KNN) etc.', ), className="mb-2")
        ]),
       
        dbc.Row([
            dbc.Col(html.H6(children='Réseau de neurones', ), className="mb-2")
        ]),
        
        # Evaluer un modele
        
       dbc.Row([
          dbc.Col(html.H4(children='Evaluer un modèle de classification'), className="mb-2")
          ]),
          dbc.Row([
            dbc.Col(html.H6(children='Tester sur des données (vérité terrain) et  Comparer les résultats à ces dernières.', ), className="mb-2")
        ]),
         
         dbc.Row([
            dbc.Col(html.H6(children='Plusieurs métriques : Matrice de confusion, Accuracy, Précision, Rappel' ), className="mb-2")
        ]),
          
          
    ])
    ])