# app/historia_clinica/views.py

from flask import Flask, request, render_template, flash, redirect, url_for
from . import historia_clinica
from .. import db
from .historia_personal.views import get_historia_personal
from .antecedentes_familiares.views import get_antecedentes_familiares
from .frecuencia_alimentos.views import get_frecuencia_alimentos
from ..models import Actividad_fisica, Paciente

app = Flask(__name__)

## VISTAS - VER LA HISTORIA CLINICA COMPLETA DE UN PACIENTE ##
@historia_clinica.route('/ver_historia_clinica/<int:id>')
def ver_historia_clinica(id):
    historia_personal = get_historia_personal(id)
    antecedentes_familiares = get_antecedentes_familiares(id)
    frecuencia_alimentos = get_frecuencia_alimentos(id)
    actividad_fisica = Actividad_fisica.query.filter_by(paciente_id=id).first()

    paciente = Paciente.query.get_or_404(id)
    nombre_paciente = paciente.nombre
    paciente_id = paciente.id
    return render_template('historia_clinica/ver_historia_clinica.html', historia_personal=historia_personal, 
                            antecedentes_familiares=antecedentes_familiares, frecuencia_alimentos=frecuencia_alimentos, 
                            actividad_fisica=actividad_fisica, nombre_paciente=nombre_paciente, paciente_id=paciente_id, title="Ver historia clinica")

## VISTAS - COMPLETAR LOS REGISTROS DE ACTIVIDAD FISICA DE UN PACIENTE ##
@historia_clinica.route('/actividad_fisica', methods=['GET', 'POST'])
def actividad_fisica():
    if request.method == 'POST':
        actividad_fisica = Actividad_fisica(actividad=request.form['actividad'], cual_actividad=request.form['cual_actividad'], cuantas_veces=request.form['cuantas_veces'])
        db.session.add(actividad_fisica)
        db.session.commit()

        id_paciente = request.form['id']
        nombre_paciente = request.form['nombre_paciente']
        flash('Has agregado la actividad fisica del paciente'+nombre_paciente+' con éxito.')

        return render_template('home/index.html', title="Home")
    return render_template('historia_clinica/actividad_fisica.html', title="Actividad física")    

## VISTAS - EDITAR LOS REGISTROS DE ACTIVIDAD FISICA DE UN PACIENTE ##
@historia_clinica.route('/edit_actividad_fisica/<int:id>', methods=['GET', 'POST'])
def edit_actividad_fisica(id):
    actividad_fisica = Actividad_fisica.query.filter_by(paciente_id=id).first()
    if request.method == 'POST':
        update_actividad_fisica = Actividad_fisica.query.filter_by(paciente_id=id).first()
        if update_actividad_fisica == None:
            new_actividad_fisica = Actividad_fisica(actividad=request.form['actividad'], cual_actividad=request.form['cual_actividad'], 
                                                    cuantas_veces=request.form['cuantas_veces'], paciente_id=id)
            db.session.add(new_actividad_fisica)
            db.session.commit()
            flash('Has editado los registros de actividad física del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
        else:
            update_actividad_fisica.actividad = request.form['actividad']
            update_actividad_fisica.cual_actividad = request.form['cual_actividad']
            update_actividad_fisica.cuantas_veces = request.form['cuantas_veces']
            db.session.commit()
            flash('Has editado los registros de actividad física del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
    paciente = Paciente.query.filter_by(id=id).first()
    return render_template('historia_clinica/edit_actividad_fisica.html', actividad_fisica=actividad_fisica, paciente=paciente, title='Editar actividad física')



