#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc


# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.CERULEAN]#MATERIA]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Animal Research' 

server = app.server
app.config.suppress_callback_exceptions = True