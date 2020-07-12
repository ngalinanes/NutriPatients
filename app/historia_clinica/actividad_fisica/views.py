# app/historia_clinica/actividad_fisica/views.py

from flask import Flask, flash, request, redirect, url_for, render_template
from ... import db
from ...models import Actividad_fisica
from ...paciente.views import get_paciente
from . import actividad_fisica

app = Flask(__name__)

## FUNCION - OBTENER LA ACTIVIDAD FISICA DE UN PACIENTE EN PARTICULAR
def get_actividad_fisica(id):
    result = Actividad_fisica.query.filter_by(paciente_id=id).first()
    return result

## FUNCION - CREAR UNA NUEVA ACTIVIDAD FISICA PARA UN PACIENTE
def create_actividad_fisica(actividad,cual_actividad,cuantas_veces,paciente_id):
    result = Actividad_fisica(actividad=actividad, 
                            cual_actividad=cual_actividad, 
                            cuantas_veces=cuantas_veces,
                            paciente_id=paciente_id)
    db.session.add(result)
    db.session.commit()

    return result

## VISTAS - COMPLETAR LOS REGISTROS DE ACTIVIDAD FISICA DE UN PACIENTE ##
@actividad_fisica.route('/actividad_fisica', methods=['GET', 'POST'])
def nueva_actividad_fisica():
    if request.method == 'POST':
        actividad_fisica = create_actividad_fisica(request.form['actividad'],request.form['cual_actividad'],request.form['cuantas_veces'],request.form['id'])

        id_paciente = request.form['id']
        nombre_paciente = request.form['nombre_paciente']
        flash('Has agregado la actividad fisica del paciente '+nombre_paciente+' con éxito.')

        return render_template('home/index.html', title="Home")
    return render_template('historia_clinica/actividad_fisica.html', title="Actividad física")    

## VISTAS - EDITAR LOS REGISTROS DE ACTIVIDAD FISICA DE UN PACIENTE ##
@actividad_fisica.route('/edit_actividad_fisica/<int:id>', methods=['GET', 'POST'])
def edit_actividad_fisica(id):
    actividad_fisica = get_actividad_fisica(id)
    if request.method == 'POST':
        update_actividad_fisica = get_actividad_fisica(id)
        if update_actividad_fisica == None:
            new_actividad_fisica = create_actividad_fisica(request.form['actividad'],request.form['cual_actividad'], request.form['cuantas_veces'], id)
            
            flash('Has editado los registros de actividad física del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
        else:
            update_actividad_fisica.actividad = request.form['actividad']
            update_actividad_fisica.cual_actividad = request.form['cual_actividad']
            update_actividad_fisica.cuantas_veces = request.form['cuantas_veces']
            db.session.commit()
            flash('Has editado los registros de actividad física del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
    paciente = get_paciente(id)
    return render_template('historia_clinica/edit_actividad_fisica.html', actividad_fisica=actividad_fisica, paciente=paciente, title='Editar actividad física')