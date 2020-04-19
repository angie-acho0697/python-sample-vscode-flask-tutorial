from flask import Flask
import flask
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
