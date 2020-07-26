from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import Config

app = Flask(__name__)

ENV = 'production'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1012@localhost/Herolo'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bddopkefbrgpdb:f70571669f339c10761baab0b5e87a72eb0e998a6161aca0aa6f92764412662e@ec2-50-19-26-235.compute-1.amazonaws.com:5432/d2a1s4uocoas8o'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#to query our database
db = SQLAlchemy(app)
app.config.from_object(Config)

from application import routes 




