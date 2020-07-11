# app/historia_clinica/views.py

from flask import Flask, request, render_template, flash, redirect, url_for
from . import historia_clinica
from .. import db
from .historia_personal.views import get_historia_personal
from .antecedentes_familiares.views import get_antecedentes_familiares
from ..models import Actividad_fisica, Frecuencia_alimentos, Paciente

app = Flask(__name__)

## VISTAS - COMPLETAR LA FRECUENCIA DE ALIMENTOS DE UN PACIENTE ##
@historia_clinica.route('/frecuencia_alimentos', methods=['GET', 'POST'])
def frecuencia_alimentos():
    if request.method == 'POST':
        frecuencia_alimentos = Frecuencia_alimentos(
            frutas=request.form['frutas'],
            verduras=request.form['verduras'],
            carne=request.form['carne'],
            lacteos=request.form['lacteos'],
            agua=request.form['agua'],
            gaseosa=request.form['gaseosa'],
            huevo=request.form['huevo'],
            cereales=request.form['cereales'],
            casera=request.form['casera'],
            afuera=request.form['afuera'],
            paciente_id = request.form['id']
        )
        db.session.add(frecuencia_alimentos)
        db.session.commit()

        id_paciente = request.form['id']
        nombre_paciente = request.form['nombre_paciente']
        flash('Has agregado la historia personal de '+nombre_paciente+' de manera exitosa.')

        return render_template('historia_clinica/actividad_fisica.html', id=id_paciente, nombre_paciente=nombre_paciente, title="Historia clinica")
    return render_template('historia_clinica/frecuencia_alimentos.html', title='Frecuencia de alimentos')

## VISTAS - VER LA HISTORIA CLINICA COMPLETA DE UN PACIENTE ##
@historia_clinica.route('/ver_historia_clinica/<int:id>')
def ver_historia_clinica(id):
    historia_personal = get_historia_personal(id)
    antecedentes_familiares = get_antecedentes_familiares(id)
    frecuencia_alimentos = Frecuencia_alimentos.query.filter_by(paciente_id=id).first()
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

## VISTAS - EDITAR LOS REGISTROS DE FRECUENCIA DE ALIEMENTOS DE UN PACIENTE ##
@historia_clinica.route('/edit_frecuencia_alimentos/<int:id>', methods=['GET', 'POST'])
def edit_frecuencia_alimentos(id):
    frecuencia_alimentos = Frecuencia_alimentos.query.filter_by(paciente_id=id).first()
    if request.method == 'POST':
        update_frecuencia_alimentos = Frecuencia_alimentos.query.filter_by(paciente_id=id).first()
        if update_frecuencia_alimentos == None:
            new_frecuencia_alimentos = Frecuencia_alimentos(frutas=request.form['frutas'], 
                                                    verduras=request.form['verduras'], 
                                                    carnes=request.form['carne'],
                                                    lacteos=request.form['lacteos'],
                                                    agua=request.form['agua'],
                                                    gaseosa=request.form['gaseosa'],
                                                    huevo=request.form['huevo'],
                                                    cereales=request.form['cereales'],
                                                    casera=request.form['casera'],
                                                    afuera=request.form['afuera'],
                                                     paciente_id=id)
            db.session.add(new_frecuencia_alimentos)
            db.session.commit()
            flash('Has editado los registros de la frecuencia de alimentos del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
        else:
            update_frecuencia_alimentos.frutas = request.form['frutas']
            update_frecuencia_alimentos.verduras = request.form['verduras']
            update_frecuencia_alimentos.carnes = request.form['carne']
            update_frecuencia_alimentos.lacteos = request.form['lacteos']
            update_frecuencia_alimentos.agua = request.form['agua']
            update_frecuencia_alimentos.gaseosa = request.form['gaseosa']
            update_frecuencia_alimentos.huevo = request.form['huevo']
            update_frecuencia_alimentos.cereales = request.form['cereales']
            update_frecuencia_alimentos.afuera = request.form['afuera']
            db.session.commit()
            flash('Has editado los registros de la frecuencia de alimentos del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
    paciente = Paciente.query.filter_by(id=id).first()
    return render_template('historia_clinica/edit_frecuencia_alimentos.html', frecuencia_alimentos=frecuencia_alimentos, paciente=paciente, title='Editar frecuencia de alimentos')

