# app/__init__.py

# third-party imports
from flask import Flask, render_template, flash, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from flask_bootstrap import Bootstrap

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+cymysql://admin:password@localhost/mica"
    app.config["SECRET_KEY"] = 'p9Bv<3Eid9%$i01'
    app.config["ENV"] = "development"

    Bootstrap(app)
    db.init_app(app)
    migrate = Migrate(app, db)    

    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .paciente import paciente as paciente_blueprint
    app.register_blueprint(paciente_blueprint)

    from .historia_clinica import historia_clinica as historia_clinica_blueprint
    app.register_blueprint(historia_clinica_blueprint)

    from .historia_clinica.historia_personal import historia_personal as historia_personal_blueprint
    app.register_blueprint(historia_personal_blueprint)

    return app