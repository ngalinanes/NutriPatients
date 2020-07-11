from flask import request, render_template, flash, redirect, url_for
from . import paciente
from ..models import Paciente
from .. import db

## FUNCION - OBTENER UN PACIENTE EN PARTICULAR
def get_paciente(id):
    result = Paciente.query.get_or_404(id)
    return result

## VISTAS - AGREGAR NUEVO PACIENTE ##
@paciente.route('/nuevo_paciente', methods=['GET','POST'])
def nuevo_paciente():
    if request.method == 'POST':
        paciente = Paciente(
            nombre=request.form['nombre'],
            nacimiento=request.form['nacimiento'],
            edad=request.form['edad'],
            telefono=request.form['telefono'],
            estado_civil=request.form['estado_civil'],
            email=request.form['email'],
            cant_hijos=request.form['cant_hijos'],
            ocupacion=request.form['ocupacion'],
            observaciones=request.form['observaciones']
        )
        db.session.add(paciente)
        db.session.commit()
        flash('Has agregado un paciente de forma exitosa.')

        aux_paciente = Paciente.query.filter_by(email=request.form['email']).first()
        id_paciente = aux_paciente.id
        nombre_paciente = aux_paciente.nombre

        return render_template('historia_clinica/historia_personal.html', id=id_paciente, nombre_paciente=nombre_paciente, title="Historia clinica")
        #return redirect(url_for('historia_clinica', id=id_paciente, nombre_paciente=nombre_paciente))
    return render_template('pacientes/nuevo_paciente.html', title='Agregar Paciente')

## VISTAS - VER UN PACIENTE ESPECIFICO ##
@paciente.route('/ver_paciente/<int:id>', methods=['GET', 'POST'])
def ver_paciente(id):
    paciente = Paciente.query.get_or_404(id)

    return render_template('pacientes/ver_paciente.html', paciente=paciente, title="Perfil paciente")

## VISTAS - EDITAR UN PACIENTE ##
@paciente.route('/edit_paciente/<int:id>', methods=['GET', 'POST'])
def edit_paciente(id):
    paciente = Paciente.query.get_or_404(id)

    if request.method == 'POST':
        update_paciente = Paciente.query.get_or_404(id)
        update_paciente.nombre = request.form['nombre']
        update_paciente.nacimiento = request.form['nacimiento']
        update_paciente.edad = request.form['edad']
        update_paciente.telefono = request.form['telefono']
        update_paciente.estado_civil = request.form['estado_civil']
        update_paciente.email = request.form['email']
        update_paciente.cant_hijos = request.form['cant_hijos']
        update_paciente.ocupacion = request.form['ocupacion'],
        update_paciente.observaciones=request.form['observaciones']
        db.session.commit()
        flash("Has editado el paciente de manera exitosa.")
        return redirect(url_for('all_pacientes'))

    return render_template('pacientes/edit_paciente.html', paciente=paciente, title="Editar paciente")

## VISTAS - VER TODOS LOS PACIENTES ##
@paciente.route('/all_pacientes')
def all_pacientes():
    pacientes = Paciente.query.all()

    return render_template('pacientes/all_pacientes.html', pacientes=pacientes, title='Lista de pacientes')
