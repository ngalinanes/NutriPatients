# app/models.py

from app import db

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