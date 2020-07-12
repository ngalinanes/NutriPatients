# app/historia_clinica/actividad_fisica/__init__.py

from flask import Blueprint

actividad_fisica = Blueprint('actividad_fisica', __name__)

from . import views