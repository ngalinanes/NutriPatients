from flask import render_template, Flask
from . import home

app = Flask(__name__)


## VISTAS - INICIO ##
@home.route('/')
def index():
    return render_template('home/index.html', title='Inicio')