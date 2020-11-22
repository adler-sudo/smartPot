import os
import dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)

server.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
# checking to see if i hard code the database location if we can get it to fly
# server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'smartPot.db')
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/pi/secondDashing/smartPot.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)
migrate = Migrate(server, db)






app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)






