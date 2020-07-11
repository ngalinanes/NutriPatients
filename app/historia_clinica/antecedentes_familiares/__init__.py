# app/historia_clinica/antecedentes_familiares/__init__.py

from flask import Blueprint

antecedentes_familiares = Blueprint('antecedentes_familiares', __name__)

from . import views