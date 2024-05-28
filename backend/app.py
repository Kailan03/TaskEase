#!/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
cors = CORS(app)
jwt = JWTManager(app)

# Import routes after defining db, cors, and jwt to avoid circular imports
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(task_bp, url_prefix='/api/tasks')

if __name__ == '__main__':
    app.run(debug=True)

