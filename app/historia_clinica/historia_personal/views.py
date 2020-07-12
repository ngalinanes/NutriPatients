# app/historia_clinica/historia_personal/views.py

from flask import Flask, request, render_template, flash, redirect, url_for
from ...models import Historia_personal
from ... import db
from . import historia_personal
from ...paciente.views import get_paciente

app = Flask(__name__)

## FUNCION - OBTENER UNA HISTORIA PERSONAL EN PARTICULAR
def get_historia_personal(id):
    result = Historia_personal.query.filter_by(paciente_id=id).first()
    return result

## FUNCION - CREAR UNA NUEVA INSTANCIA DE HISTORIA PERSONAL
def create_historia_personal(enfermedades_cronicas,obs_enf_cron,cirugias,obs_cirugias,alergias,obs_alergias,med_psiquiatrica,obs_med_psiquiatrica,otra_med,obs_otra_med,tabaco,obs_tabaco,alcohol,obs_alcohol,drogas, obs_drogas,paciente_id):
    result = Historia_personal(
            enfermedades_cronicas=enfermedades_cronicas,
            obs_enf_cron=obs_enf_cron,
            cirugias=cirugias,
            obs_cirugias=obs_cirugias,
            alergias=alergias,
            obs_alergias=obs_alergias,
            med_psiquiatrica=med_psiquiatrica,
            obs_med_psiquiatrica=obs_med_psiquiatrica,
            otra_med=otra_med,
            obs_otra_med=obs_otra_med,
            tabaco=tabaco,
            obs_tabaco=obs_tabaco,
            alcohol=alcohol,
            obs_alcohol=obs_alcohol,
            drogas=drogas,
            obs_drogas=obs_drogas,
            paciente_id=paciente_id
    )
    db.session.add(result)
    db.session.commit()

    return result

## VISTAS - NUEVA HISTORIA PERSONAL
@historia_personal.route('/nueva_historia_personal', methods=['GET', 'POST'])
def nueva_historia_personal():
    if request.method == 'POST':
        historia_personal = create_historia_personal(
            request.form['enfermedades_cronicas'],
            request.form['obs_enf_cron'],
            request.form['cirugias'],
            request.form['obs_cirugias'],
            request.form['alergias'],
            request.form['obs_alergias'],
            request.form['med_psiquiatrica'],
            request.form['obs_med_psiquiatrica'],
            request.form['otra_med'],
            request.form['obs_otra_med'],
            request.form['tabaco'],
            request.form['obs_tabaco'],
            request.form['alcohol'],
            request.form['obs_alcohol'],
            request.form['drogas'],
            request.form['obs_drogas'],
            request.form['id']
        )
        
        id_paciente = request.form['id']
        nombre_paciente = request.form['nombre_paciente']
        flash('Has agregado la historia personal de '+nombre_paciente+' de manera exitosa.')

        return render_template('historia_clinica/antecedentes_familiares.html', id=id_paciente, nombre_paciente=nombre_paciente, title="Historia clinica")
    return render_template('historia_clinica/historia_personal.html', title='Historia personal')    

## VISTAS - EDITAR LA HISTORIA PERSONAL DE UN PACIENTE ##
@historia_personal.route('/edit_historia_personal/<int:id>', methods=['GET', 'POST'])
def edit_historia_personal(id):
    historia_personal = get_historia_personal(id)
    if request.method == 'POST':
        update_historia_personal = get_historia_personal(id)
        if update_historia_personal == None:
            new_historia_personal = create_historia_personal(
            request.form['enfermedades_cronicas'],
            request.form['obs_enf_cron'],
            request.form['cirugias'],
            request.form['obs_cirugias'],
            request.form['alergias'],
            request.form['obs_alergias'],
            request.form['med_psiquiatrica'],
            request.form['obs_med_psiquiatrica'],
            request.form['otra_med'],
            request.form['obs_otra_med'],
            request.form['tabaco'],
            request.form['obs_tabaco'],
            request.form['alcohol'],
            request.form['obs_alcohol'],
            request.form['drogas'],
            request.form['obs_drogas'],
            id
        )
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
            return redirect(url_for('historia_clinica.ver_historia_clinica', id=id))
    paciente = get_paciente(id)
    return render_template('historia_clinica/edit_historia_personal.html', historia_personal=historia_personal, paciente=paciente, title='Editar historia personal')