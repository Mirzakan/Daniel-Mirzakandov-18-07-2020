from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import Config

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1012@localhost/Herolo'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qndnjcxekqlmnk:315344415ba2a420b5a3b2152e21075b53af94b495eaec136485b72389475c5d@ec2-3-230-106-126.compute-1.amazonaws.com:5432/d25tfv6rs09gvf'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#to query our database
db = SQLAlchemy(app)
app.config.from_object(Config)

from application import routes 




