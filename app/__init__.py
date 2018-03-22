# app/__init__.py

from flask import Flask 

# intialize

app = Flask(__name__, instance_relative_config=True)

# load  the views

from app import views


#load  the config file

app.config.from_object('config')
