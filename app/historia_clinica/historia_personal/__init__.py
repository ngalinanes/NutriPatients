# app/historia_clinica/historia_personal/__init__.py

from flask import Blueprint

historia_personal = Blueprint('historia_personal', __name__)

from . import views