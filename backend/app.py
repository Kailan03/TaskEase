#!/bin/env python3

# This Flask Web Application
#
# This is the main application file that sets up the Flask web application,
# configures the database connection, and registers the various blueprints
# for handling different types of requests.
#
# The application is configured using the config.py file, which contains
# environment-specific settings such as the database connection details,
# JWT secret key, and other configuration parameters.
#
# The application uses the following blueprints:
# - auth_bp: Handles user authentication-related routes (login, logout, registration, etc.)
# - task_bp: Handles CRUD operations for user tasks
#
# The application also uses the following extensions:
# - SQLAlchemy: For database management and ORM (Object-Relational Mapping)
# - CORS: For enabling Cross-Origin Resource Sharing
# - JWTManager: For handling JSON Web Tokens for authentication

from flask import Flask,Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import config
from routes.auth_routes import auth_bp
from routes.extensions import db
from routes.task_routes import task_bp

# This section initializes the main Flask application object and configures it
# using the settings defined in the config.py file.

app = Flask(__name__) 
app.config.from_object(config)

# Initializes the SQLAlchemy extension, which  provides an ORM 
# (Object-Relational Mapping) layer for interacting with the database.

db = SQLAlchemy(app)

# Imports the User model from the models package, which defines the database
# schema for user-related data.
from models.user import User

cors = CORS(app)
jwt = JWTManager(app)

 ###############################################

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle the form submission
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if password != confirm_password:
            return jsonify({'message': 'Passwords do not match!'}), 400

        # Add user registration logic here (e.g., saving to the database)
        # After successful registration, send a JSON response
        return jsonify({'message': 'Registration successful!'})
    return render_template('register.html') 
 
 ###############################################

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Process login form submission
        # Extract data from request.form and perform necessary actions
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            return redirect(url_for('dashboard'))
    else:
        flash('Login Unsuccessful. Please check email and password')
        # Render the login form template for GET requests
    return render_template('login.html')

# from routes.task_routes import task_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
# app.register_blueprint(task_bp, url_prefix='/api/tasks')

# Landing page loading 
@app.route('/')
def landing_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
