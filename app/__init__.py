# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
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

    from .historia_clinica.antecedentes_familiares import antecedentes_familiares as antecedentes_familiares_blueprint
    app.register_blueprint(antecedentes_familiares_blueprint)

    from .historia_clinica.frecuencia_alimentos import frecuencia_alimentos as frecuencia_alimentos_blueprint
    app.register_blueprint(frecuencia_alimentos_blueprint)

    return app