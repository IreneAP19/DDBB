import pandas as pd

#Esta funcion pivota los datos de origen de los csv de clase poder pasar los proyectos de columna a filas y así facilitar el concatenado de tablas e ingesta en BBDD
def class_melt(clase):
    return pd.melt(
    clase,
    id_vars=["Nombre", "Email", "Promoción", "Fecha_comienzo", "Campus"], 
    value_vars=[i for i in pd.DataFrame(clase.columns).loc[pd.DataFrame(clase.columns)[0].str.contains("Proyecto"), 0]], 
    var_name="Proyecto",  
    value_name="Calificación")


#Definimos primero un diccionario de Verticales (vertical_rules), que se deberá actualizar en caso de de ampliar oferta Formativa:
vertical_rules = {
    "FS": ['Proyecto_WebDev', 'Proyecto_FrontEnd', 'Proyecto_Backend', 
           'Proyecto_React', 'Proyecto_FullSatck'],
    "DS": ['Proyecto_HLF', 'Proyecto_EDA', 'Proyecto_BBDD', 'Proyecto_ML',
       'Proyecto_Deployment']
}
#Esta funcion el proyecto del alumno y lo checkea dentro del vertical_rules para identificar la vertical a la que pertenece
def asignar_vertical(proyecto):
    for vertical, proyectos in vertical_rules.items():
        if proyecto in proyectos:
            return vertical
    return 'Desconocido'