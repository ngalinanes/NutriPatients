# app/historia_clinica/frecuencia_alimentos/views.py

from flask import Flask, request, render_template, url_for, redirect, flash
from . import frecuencia_alimentos
from ... import db
from ...models import Frecuencia_alimentos, Paciente

app = Flask(__name__)

## FUNCION - OBTENER LA FRECUENCIA DE ALIMENTOS DE UN PACIENTE EN PARTICULAR
def get_frecuencia_alimentos(id):
    result = Frecuencia_alimentos.query.filter_by(paciente_id=id).first()
    return result

## VISTAS - COMPLETAR LA FRECUENCIA DE ALIMENTOS DE UN PACIENTE ##
@frecuencia_alimentos.route('/frecuencia_alimentos', methods=['GET', 'POST'])
def nueva_frecuencia_alimentos():
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

## VISTAS - EDITAR LOS REGISTROS DE FRECUENCIA DE ALIEMENTOS DE UN PACIENTE ##
@frecuencia_alimentos.route('/edit_frecuencia_alimentos/<int:id>', methods=['GET', 'POST'])
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