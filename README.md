# NutriPatients
Proyecto propio

WebApp para el manejo de pacientes con sus historias clinicas nutricionales. Hecha en Python3, Flask, Jinja2, MySQL.

Probado desde Linux Ubuntu 18.04 corriendo sobre Windows 10 (Windows Subsystem for Linux)

## Ambiente a instalar:
-   Python 3.6
-   python3-venv
-   pip3
-   Motor de base de datos (En mi caso use MySQL, con una base previamente creada llamada "mica")
-   Usuario de MySQL (a modo de prueba estoy usando admin:password dentro del mismo app.py, no recomendable en prod).

## Como correr la app por primera vez:
-   Se debe crear un ambiente virtual de Python 3. NOTA: Recomiendo usar como nombre "venv" ya que se encuentra excluido en el .gitignore, de usar otro nombre tener en cuenta de actualzarlo o crearlo fuera del repositorio.

$ python3 -m venv <nombre-del-venv>

-   Activo el ambiente virtual

$ source <nombre-del-venv>/bin/activate

-   Instalar las dependencias de la app

$ pip3 install -r requirements.txt

-   Inicializar la base

$ flask db init

-   Migrar los modelos a la base

$ flask db migrate

- Actualizar los cambios

$ flask db upgrade

- Iniciamos la app

$ python3 run.py
