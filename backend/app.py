#!/bin/env python3
from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from extensions import db 

app = Flask(__name__)
auth_bp = Blueprint('auth', __name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

#@auth_bp.route('/login', methods=['GET', 'POST'])
#def login():
#   return render_template('login.html')

app.config.from_object(Config)

db = SQLAlchemy(app)
cors = CORS(app)
jwt = JWTManager(app)

from routes import auth_routes, task_routes

app.register_blueprint(auth_routes.auth_bp, url_prefix='/api/auth')
app.register_blueprint(task_routes.task_bp, url_prefix='/api/tasks')

if __name__ == '__main__':
    app.run(debug=True)

