from flask import Flask, request, render_template, flash, redirect, url_for
from ...models import Historia_personal, Paciente
from ... import db
from . import historia_personal

app = Flask(__name__)

## FUNCION - OBTENER UNA HISTORIA PERSONAL EN PARTICULAR
def get_historia_personal(id):
    result = Historia_personal.query.filter_by(paciente_id=id).first()
    return result

## VISTAS - NUEVA HISTORIA PERSONAL
@historia_personal.route('/nueva_historia_personal', methods=['GET', 'POST'])
def nueva_historia_personal():
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
    return render_template('historia_clinica/historia_personal.html', title='Historia personal')    

## VISTAS - EDITAR LA HISTORIA PERSONAL DE UN PACIENTE ##
@historia_personal.route('/edit_historia_personal/<int:id>', methods=['GET', 'POST'])
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
    return render_template('historia_clinica/edit_historia_personal.html', historia_personal=historia_personal, paciente=paciente, title='Editar historia personal')