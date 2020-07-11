# app/historia_clinica/antecedentes_familiares/views.py

from flask import Flask, render_template, flash, request, url_for, redirect
from . import antecedentes_familiares
from ... import db
from ...models import Antecedentes_familiares, Paciente

app = Flask(__name__)

## FUNCION - OBTENER LOS ANTECEDENTES FAMILIARES DE UN PACIENTE EN PARTICULAR
def get_antecedentes_familiares(id):
    result = Antecedentes_familiares.query.filter_by(paciente_id=id).first()
    return result
    
## VISTAS - COMPLETAR LOS ANTECEDENTES FAMILIARES DE UN PACIENTE ##
@antecedentes_familiares.route('/antecedentes_familiares', methods=['GET', 'POST'])
def nuevo_antecedentes_familiares():
    if request.method == 'POST':
        antecedentes_familiares = Antecedentes_familiares(
            diabetes=request.form['diabetes'],
            cardiaca=request.form['cardiaca'],
            hipertension=request.form['hipertension'],
            sobrepeso=request.form['sobrepeso'],
            acv=request.form['acv'],
            cancer=request.form['cancer'],
            observaciones=request.form['observaciones'],
            otro_tca=request.form['otro_tca'],
            paciente_id = request.form['id']
        )
        db.session.add(antecedentes_familiares)
        db.session.commit()

        id_paciente = request.form['id']
        nombre_paciente = request.form['nombre_paciente']
        flash('Has agregado los antecedentes familiares de '+nombre_paciente+' de manera exitosa.')

        return render_template('historia_clinica/frecuencia_alimentos.html', id=id_paciente, nombre_paciente=nombre_paciente, title="Historia clinica")
    return render_template('historia_clinica/antecedentes_familiares.html', title='Antecedentes familiares')

## VISTAS - EDITAR LOS ANTECEDENTES FAMILIARES DE UN PACIENTE ##
@antecedentes_familiares.route('/edit_antecedentes_familiares/<int:id>', methods=['GET', 'POST'])
def edit_antecedentes_familiares(id):
    antecedentes_familiares = Antecedentes_familiares.query.filter_by(paciente_id=id).first()
    if request.method == 'POST':
        update_antecedentes_familiares = Antecedentes_familiares.query.filter_by(paciente_id=id).first()
        if update_antecedentes_familiares == None:
            new_antecedentes_familiares = Antecedentes_familiares(diabetes=request.form['diabetes'],
                                                                cardiaca=request.form['cardiaca'],
                                                                hipertension=request.form['hipertension'],
                                                                sobrepeso=request.form['sobrepeso'],
                                                                acv=request.form['acv'],
                                                                cancer=request.form['cancer'],
                                                                observaciones=request.form['observaciones'],
                                                                otro_tca=request.form['otro_tca'], 
                                                                paciente_id=id)
            db.session.add(new_antecedentes_familiares)
            db.session.commit()
            flash('Has editado los antecedentes familiares del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
        else:
            update_antecedentes_familiares.diabetes = request.form['diabetes']
            update_antecedentes_familiares.cardiaca = request.form['cardiaca']
            update_antecedentes_familiares.hipertension = request.form['hipertension']
            update_antecedentes_familiares.sobrepeso = request.form['sobrepeso']
            update_antecedentes_familiares.acv = request.form['acv']
            update_antecedentes_familiares.cancer = request.form['cancer']
            update_antecedentes_familiares.observaciones = request.form['observaciones']
            update_antecedentes_familiares.otro_tca = request.form['otro_tca']
            update_antecedentes_familiares.paciente_id = id
            db.session.commit()
            flash('Has editado los antecedentes familiares del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
    paciente = Paciente.query.filter_by(id=id).first()
    return render_template('historia_clinica/edit_antecedentes_familiares.html', antecedentes_familiares=antecedentes_familiares, paciente=paciente, title='Editar antecedentes familiares')