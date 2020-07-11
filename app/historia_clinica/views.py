from flask import Flask, request, render_template, flash, redirect, url_for
from . import historia_clinica
from .. import db
from ..models import Historia_personal, Actividad_fisica, Antecedentes_familiares, Frecuencia_alimentos, Paciente

app = Flask(__name__)


## VISTAS - COMPLETAR EL HISTORIAL PERSONAL DE UN PACIENTE ##
@historia_clinica.route('/historia_personal', methods=['GET', 'POST'])
def historia_personal():
    if request.method == 'POST':
        historia_personal = Historia_personal(
            enfermedades_cronicas=request.form['enfermedades_cronicas'],
            obs_enf_cron=request.form['obs_enf_cron'],
            cirugias=request.form['cirugias'],
            obs_cirugias=request.form['obs_cirugias'],
            alergias=request.form['alergias'],
            obs_alergias=request.form['obs_alergias'],
            med_psiquiatrica=request.form['med_psiquiatrica'],
            obs_med_psiquiatrica=request.form['obs_med_psiquiatrica'],
            otra_med=request.form['otra_med'],
            obs_otra_med=request.form['obs_otra_med'],
            tabaco=request.form['tabaco'],
            obs_tabaco=request.form['obs_tabaco'],
            alcohol = request.form['alcohol'],
            obs_alcohol = request.form['obs_alcohol'],
            drogas=request.form['drogas'],
            obs_drogas=request.form['obs_drogas'],
            paciente_id = request.form['id']
        )
        db.session.add(historia_personal)
        db.session.commit()

        id_paciente = request.form['id']
        nombre_paciente = request.form['nombre_paciente']
        flash('Has agregado la historia personal de '+nombre_paciente+' de manera exitosa.')

        return render_template('historia_clinica/antecedentes_familiares.html', id=id_paciente, nombre_paciente=nombre_paciente, title="Historia clinica")
    return render_template('historia_clinica/historia_personal.html', title='Historia Clinica')

## VISTAS - COMPLETAR LOS ANTECEDENTES FAMILIARES DE UN PACIENTE ##
@historia_clinica.route('/antecedentes_familiares', methods=['GET', 'POST'])
def antecedentes_familiares():
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
    historia_personal = Historia_personal.query.filter_by(paciente_id=id).first()
    antecedentes_familiares = Antecedentes_familiares.query.filter_by(paciente_id=id).first()
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

## VISTAS - EDITAR LA HISTORIA PERSONAL DE UN PACIENTE ##
@historia_clinica.route('/edit_historia_personal/<int:id>', methods=['GET', 'POST'])
def edit_historia_personal(id):
    historia_personal = Historia_personal.query.filter_by(paciente_id=id).first()
    if request.method == 'POST':
        update_historia_personal = Historia_personal.query.filter_by(paciente_id=id).first()
        if update_historia_personal == None:
            new_historia_personal = Historia_personal(
            enfermedades_cronicas=request.form['enfermedades_cronicas'],
            obs_enf_cron=request.form['obs_enf_cron'],
            cirugias=request.form['cirugias'],
            obs_cirugias=request.form['obs_cirugias'],
            alergias=request.form['alergias'],
            obs_alergias=request.form['obs_alergias'],
            med_psiquiatrica=request.form['med_psiquiatrica'],
            obs_med_psiquiatrica=request.form['obs_med_psiquiatrica'],
            otra_med=request.form['otra_med'],
            obs_otra_med=request.form['obs_otra_med'],
            tabaco=request.form['tabaco'],
            obs_tabaco=request.form['obs_tabaco'],
            alcohol = request.form['alcohol'],
            obs_alcohol = request.form['obs_alcohol'],
            drogas=request.form['drogas'],
            obs_drogas=request.form['obs_drogas'],
            paciente_id=id)
            db.session.add(new_historia_personal)
            db.session.commit()
            flash('Has editado la historia personal del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
        else:
            update_historia_personal.enfermedades_cronicas = request.form['enfermedades_cronicas']
            update_historia_personal.obs_enf_cron = request.form['obs_enf_cron']
            update_historia_personal.cirugias = request.form['cirugias']
            update_historia_personal.obs_cirugias = request.form['obs_cirugias']
            update_historia_personal.alergias = request.form['alergias']
            update_historia_personal.obs_alergias = request.form['obs_alergias']
            update_historia_personal.med_psiquiatrica = request.form['med_psiquiatrica']
            update_historia_personal.obs_med_psiquiatrica = request.form['obs_med_psiquiatrica']
            update_historia_personal.otra_med = request.form['otra_med']
            update_historia_personal.obs_otra_med = request.form['obs_otra_med']
            update_historia_personal.tabaco = request.form['tabaco']
            update_historia_personal.obs_tabaco = request.form['obs_tabaco']
            update_historia_personal.alcohol = request.form['alcohol']
            update_historia_personal.obs_alcohol = request.form['obs_alcohol']
            update_historia_personal.drogas = request.form['drogas']
            update_historia_personal.obs_drogas = request.form['obs_drogas']
            update_historia_personal.paciente_id = id
            db.session.commit()
            flash('Has editado la historia personal del paciente con éxito.')
            return redirect(url_for('ver_historia_clinica', id=id))
    paciente = Paciente.query.filter_by(id=id).first()
    return render_template('historia_clinica/edit_historia_personal.html', historia_personal=historia_personal, paciente=paciente, title='Editar actividad física')

## VISTAS - EDITAR LOS ANTECEDENTES FAMILIARES DE UN PACIENTE ##
@historia_clinica.route('/edit_antecedentes_familiares/<int:id>', methods=['GET', 'POST'])
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