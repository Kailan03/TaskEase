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

from routes import auth_routes, task_routes

app.register_blueprint(auth_routes.auth_bp, url_prefix='/api/auth')
app.register_blueprint(task_routes.task_bp, url_prefix='/api/tasks')

if __name__ == '__main__':
    app.run(debug=True)

