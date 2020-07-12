# app/historia_clinica/frecuencia_alimentos/views.py

from flask import Flask, request, render_template, url_for, redirect, flash
from . import frecuencia_alimentos
from ... import db
from ...models import Frecuencia_alimentos
from ...paciente.views import get_paciente

app = Flask(__name__)

## FUNCION - OBTENER LA FRECUENCIA DE ALIMENTOS DE UN PACIENTE EN PARTICULAR
def get_frecuencia_alimentos(id):
    result = Frecuencia_alimentos.query.filter_by(paciente_id=id).first()
    return result

## FUNCION - CREAR UNA INSTANCIA DE FRECUENCIA DE ALIMENTOS DE UN PACIENTE
def create_frecuencia_alimentos(frutas,verduras,carne,lacteos,agua,gaseosa,huevo,cereales,casera,afuera,paciente_id):
    result = Frecuencia_alimentos(
            frutas=frutas,
            verduras=verduras,
            carne=carne,
            lacteos=lacteos,
            agua=agua,
            gaseosa=gaseosa,
            huevo=huevo,
            cereales=cereales,
            casera=casera,
            afuera=afuera,
            paciente_id=paciente_id
    )
    db.session.add(result)
    db.session.commit()

    return result

## VISTAS - COMPLETAR LA FRECUENCIA DE ALIMENTOS DE UN PACIENTE ##
@frecuencia_alimentos.route('/frecuencia_alimentos', methods=['GET', 'POST'])
def nueva_frecuencia_alimentos():
    if request.method == 'POST':
        frecuencia_alimentos = create_frecuencia_alimentos(
            request.form['frutas'],
            request.form['verduras'],
            request.form['carne'],
            request.form['lacteos'],
            request.form['agua'],
            request.form['gaseosa'],
            request.form['huevo'],
            request.form['cereales'],
            request.form['casera'],
            request.form['afuera'],
            request.form['id']
        )

        id_paciente = request.form['id']
        nombre_paciente = request.form['nombre_paciente']
        flash('Has agregado la frecuencia de alimentos de '+nombre_paciente+' de manera exitosa.')

        return render_template('historia_clinica/actividad_fisica.html', id=id_paciente, nombre_paciente=nombre_paciente, title="Historia clinica")
    return render_template('historia_clinica/frecuencia_alimentos.html', title='Frecuencia de alimentos')

## VISTAS - EDITAR LOS REGISTROS DE FRECUENCIA DE ALIEMENTOS DE UN PACIENTE ##
@frecuencia_alimentos.route('/edit_frecuencia_alimentos/<int:id>', methods=['GET', 'POST'])
def edit_frecuencia_alimentos(id):
    frecuencia_alimentos = get_frecuencia_alimentos(id)
    if request.method == 'POST':
        update_frecuencia_alimentos = get_frecuencia_alimentos(id)
        if update_frecuencia_alimentos == None:
            new_frecuencia_alimentos = create_frecuencia_alimentos(
                request.form['frutas'],
                request.form['verduras'],
                request.form['carne'],
                request.form['lacteos'],
                request.form['agua'],
                request.form['gaseosa'],
                request.form['huevo'],
                request.form['cereales'],
                request.form['casera'],
                request.form['afuera'],
                request.form['id']
            )
            flash('Has editado los registros de la frecuencia de alimentos del paciente con éxito.')
            return redirect(url_for('historia_clinica.ver_historia_clinica', id=id))
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
            return redirect(url_for('historia_clinica.ver_historia_clinica', id=id))
    paciente = get_paciente(id)
    return render_template('historia_clinica/edit_frecuencia_alimentos.html', frecuencia_alimentos=frecuencia_alimentos, paciente=paciente, title='Editar frecuencia de alimentos')