from flask import Flask, render_template, flash, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+cymysql://admin:password@localhost/mica"
app.config["SECRET_KEY"] = 'p9Bv<3Eid9%$i01'
app.config["ENV"] = "development"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)

## MODEL - TABLA DE PACIENTES ##
class Paciente(db.Model):
    """
    Tabla pacientes
    """
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), index=True)
    nacimiento = db.Column(db.Date)
    edad = db.Column(db.Integer, index=True)
    telefono = db.Column(db.String(60), index=True)
    estado_civil = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60), unique=True, index=True, nullable=True)
    cant_hijos = db.Column(db.Integer, index=True)
    ocupacion = db.Column(db.String(60), index=True, nullable=True)
    observaciones = db.Column(db.String(60), index=True, nullable=True, default='Sin observaciones')

## MODEL - TABLA DE HISTORIA PERSONAL ##
class Historia_personal(db.Model):
    """
    Tabla historia_personal
    """
    __tablename__ = 'historia_personal'

    id = db.Column(db.Integer, primary_key=True)
    enfermedades_cronicas = db.Column(db.String(5), index=True)
    obs_enf_cron = db.Column(db.String(60), index=True, default='Sin observaciones')
    cirugias = db.Column(db.String(5), index=True)
    obs_cirugias = db.Column(db.String(60), index=True, default='Sin observaciones')
    alergias = db.Column(db.String(5), index=True)
    obs_alergias = db.Column(db.String(60), index=True, default='Sin observaciones')
    med_psiquiatrica = db.Column(db.String(5), index=True)
    obs_med_psiquiatrica = db.Column(db.String(60), index=True, default='Sin observaciones')
    otra_med = db.Column(db.String(5), index=True)
    obs_otra_med = db.Column(db.String(60), index=True, default='Sin observaciones')
    tabaco = db.Column(db.String(5), index=True)
    obs_tabaco = db.Column(db.String(60), index=True, default='Sin observaciones')
    alcohol = db.Column(db.String(5), index=True)
    obs_alcohol = db.Column(db.String(60), index=True, default='Sin observaciones')
    drogas = db.Column(db.String(5), index=True)
    obs_drogas = db.Column(db.String(60), index=True, default='Sin observaciones')
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))

## MODEL - TABLA DE ANTECENDETES FAMILIARES ##
class Antecedentes_familiares(db.Model):
    """
    Tabla de antecendetes familiares
    """
    __tablename__ = 'antecedentes_familiares'

    id = db.Column(db.Integer, primary_key=True)
    diabetes = db.Column(db.String(30), index=True)
    cardiaca = db.Column(db.String(30), index=True)
    hipertension = db.Column(db.String(30), index=True)
    sobrepeso = db.Column(db.String(30), index=True)
    acv = db.Column(db.String(30), index=True)
    cancer = db.Column(db.String(30), index=True)
    observaciones = db.Column(db.String(60), index=True, default='Sin observaciones')
    otro_tca = db.Column(db.String(40), index=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))

## MODEL - TABLA DE FRECUENCIA DE ALIMENTOS ##
class Frecuencia_alimentos(db.Model):
    """
    Tabla de frecuencia de alimentos
    """
    __tablename__ = 'frecuencia de alimentos'

    id = db.Column(db.Integer, primary_key=True)
    frutas = db.Column(db.String(30), index=True)
    verduras = db.Column(db.String(30), index=True)
    carne = db.Column(db.String(30), index=True)
    lacteos = db.Column(db.String(30), index=True)
    agua = db.Column(db.String(30), index=True)
    gaseosa = db.Column(db.String(30), index=True)
    huevo = db.Column(db.String(30), index=True)
    cereales = db.Column(db.String(30), index=True)
    casera = db.Column(db.String(30), index=True)
    afuera = db.Column(db.String(30), index=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))

## MODEL - TABLA DE ACTIVIDAD FISICA ##
class Actividad_fisica(db.Model):
    """
    Tabla de actividad fisica de pacientes
    """
    __tablename__ = 'actividad_fisica'

    id = db.Column(db.Integer, primary_key=True)
    actividad = db.Column(db.String(30), index=True)
    cual_actividad = db.Column(db.String(60), index=True)
    cuantas_veces = db.Column(db.String(80), index=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))

## VISTAS - INICIO ##
@app.route('/')
def index():
    return render_template('home/index.html', title='Inicio')

## VISTAS - AGREGAR NUEVO PACIENTE ##
@app.route('/nuevo_paciente', methods=['GET','POST'])
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
@app.route('/ver_paciente/<int:id>', methods=['GET', 'POST'])
def ver_paciente(id):
    paciente = Paciente.query.get_or_404(id)

    return render_template('pacientes/ver_paciente.html', paciente=paciente, title="Perfil paciente")

## VISTAS - EDITAR UN PACIENTE ##
@app.route('/edit_paciente/<int:id>', methods=['GET', 'POST'])
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
@app.route('/all_pacientes')
def all_pacientes():
    pacientes = Paciente.query.all()

    return render_template('pacientes/all_pacientes.html', pacientes=pacientes, title='Lista de pacientes')

## VISTAS - COMPLETAR EL HISTORIAL PERSONAL DE UN PACIENTE ##
@app.route('/historia_personal', methods=['GET', 'POST'])
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
@app.route('/antecedentes_familiares', methods=['GET', 'POST'])
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
@app.route('/frecuencia_alimentos', methods=['GET', 'POST'])
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
@app.route('/ver_historia_clinica/<int:id>')
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
@app.route('/actividad_fisica', methods=['GET', 'POST'])
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
@app.route('/edit_actividad_fisica/<int:id>', methods=['GET', 'POST'])
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
@app.route('/edit_frecuencia_alimentos/<int:id>', methods=['GET', 'POST'])
def edit_frecuencia_alimentos(id):
    frecuencia_alimentos = Frecuencia_alimentos.query.filter_by(paciente_id=id).first()
    if request.method == 'POST':
        update_frecuencia_alimentos = Frecuencia_alimentos.query.filter_by(paciente_id=id).first()
        if update_frecuencia_alimentos == None:
            new_frecuencia_alimentos = Frecuencia_alimentos(frutas=request.form['frutas'], 
                                                    verduras=request.form['verduras'], 
                                                    carnes=request.form['carnes'],
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
            update_frecuencia_alimentos.carnes = request.form['carnes']
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
    return render_template('historia_clinica/edit_frecuencia_alimentos.html', actividad_fisica=frecuencia_alimentos, paciente=paciente, title='Editar actividad física')

## VISTAS - EDITAR LA HISTORIA PERSONAL DE UN PACIENTE ##
@app.route('/edit_historia_personal/<int:id>', methods=['GET', 'POST'])
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
@app.route('/edit_antecedentes_familiares/<int:id>', methods=['GET', 'POST'])
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

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
 