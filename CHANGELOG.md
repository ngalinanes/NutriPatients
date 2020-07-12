# Change Log

## 1.2.0 (2020-07-12)
### Features
-   Se cambio la estructura interna de la app adoptando las mejores practicas recomendadas para Flask

### BugFixed
-   Se corrigieron algunos errores en el endpoint y template de actividad_fisica durante la reestructuracion de al app. (bug#1/actividad_fisica)
-   Se corrigieron algunos errores en el endpoint de frecuencia_alimentos durante la reestructuracion de al app. (bug#2/frecuencia_alimentos)
-   Se corrigieron algunos errores en el endpoint y template de historia_personal durante la reestructuracion de al app. (bug#3/error_edit_historia_personal)
-   Se corrigio una restriccion en el modelo Paciente para que varios pacientes puedan tener un mismo email. (bug#4/restriccion_mail_paciente)
-   Se corrigieron algunos errores en el template de frecuencia_alimentos para que se carguen los formularios con todos los campos cargados. (bug#5/frecuencia_alimentos_required)

## 1.0.0 (2020-07-12)
Primer release
### Features
-   ABM para carga de pacientes con sus datos personales.
-   ABM para carga de historia clinica de pacientes (Historia Personal/Antecedentes familiares/Frecuencia de alimentos/Actividad fisica).
-   Listado de todos los pacientes con sus historias clinicas.