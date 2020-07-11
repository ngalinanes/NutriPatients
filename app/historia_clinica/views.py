# app/historia_clinica/views.py

from flask import Flask, request, render_template, flash, redirect, url_for
from . import historia_clinica
from .. import db
from .historia_personal.views import get_historia_personal
from .antecedentes_familiares.views import get_antecedentes_familiares
from .frecuencia_alimentos.views import get_frecuencia_alimentos
from .actividad_fisica.views import get_actividad_fisica
from ..paciente.views import get_paciente

app = Flask(__name__)

## VISTAS - VER LA HISTORIA CLINICA COMPLETA DE UN PACIENTE ##
@historia_clinica.route('/ver_historia_clinica/<int:id>')
def ver_historia_clinica(id):
    historia_personal = get_historia_personal(id)
    antecedentes_familiares = get_antecedentes_familiares(id)
    frecuencia_alimentos = get_frecuencia_alimentos(id)
    actividad_fisica = get_actividad_fisica(id)

    paciente = get_paciente(id)
    nombre_paciente = paciente.nombre
    paciente_id = paciente.id
    return render_template('historia_clinica/ver_historia_clinica.html', historia_personal=historia_personal, 
                            antecedentes_familiares=antecedentes_familiares, frecuencia_alimentos=frecuencia_alimentos, 
                            actividad_fisica=actividad_fisica, nombre_paciente=nombre_paciente, paciente_id=paciente_id, title="Ver historia clinica")





