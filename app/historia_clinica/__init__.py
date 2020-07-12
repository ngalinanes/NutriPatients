# app/historia_clinica/__init__.py

from flask import Blueprint

historia_clinica = Blueprint('historia_clinica', __name__)

from . import views