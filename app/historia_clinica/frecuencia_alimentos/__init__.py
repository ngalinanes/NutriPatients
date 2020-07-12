# app/historia_clinica/frecuencia_alimentos/__init__.py

from flask import Blueprint

frecuencia_alimentos = Blueprint('frecuencia_alimentos', __name__)

from . import views