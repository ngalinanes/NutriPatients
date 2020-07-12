# app/paciente/__init__.py

from flask import Blueprint

paciente = Blueprint('paciente', __name__)

from . import views