from flask import render_template, request
from backend.Modelos.database import db
from backend.Modelos.Tienda import Tienda

def encuentranos():
    # Obtener todos los países únicos desde la base de datos
    paises = db.session.query(Tienda.pais).distinct().all()

    # Obtener los parámetros de consulta (como país, provincia, ciudad)
    pais_seleccionado = request.args.get('pais', '')
    provincia_seleccionada = request.args.get('provincia', '')
    ciudad_seleccionada = request.args.get('ciudad', '')

    # Filtrar provincias según el país seleccionado
    if pais_seleccionado:
        provincias = db.session.query(Tienda.provincia)\
            .filter(Tienda.pais == pais_seleccionado)\
            .distinct().all()
    else:
        provincias = db.session.query(Tienda.provincia).distinct().all()

    # Filtrar ciudades según la provincia seleccionada
    if provincia_seleccionada:
        ciudades = db.session.query(Tienda.ciudad)\
            .filter(Tienda.provincia == provincia_seleccionada)\
            .distinct().all()
    else:
        ciudades = db.session.query(Tienda.ciudad).distinct().all()

    # Crear la consulta para obtener las tiendas filtradas
    tiendas_query = Tienda.query

    # Aplicar filtros según la selección del usuario
    if pais_seleccionado:
        tiendas_query = tiendas_query.filter(Tienda.pais == pais_seleccionado)
    if provincia_seleccionada:
        tiendas_query = tiendas_query.filter(Tienda.provincia == provincia_seleccionada)
    if ciudad_seleccionada:
        tiendas_query = tiendas_query.filter(Tienda.ciudad == ciudad_seleccionada)

    # Obtener todas las tiendas filtradas
    tiendas = tiendas_query.all()


    # Pasar los datos a la plantilla
    return render_template(
        'user/encuentranos.html',
        paises=paises,
        provincias=provincias,
        ciudades=ciudades,
        tiendas=tiendas,
        selected_pais=pais_seleccionado,
        selected_provincia=provincia_seleccionada,
        selected_ciudad=ciudad_seleccionada
    )
