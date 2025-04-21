import datetime
from flask import render_template, request, session, redirect, url_for
from backend.Modelos.MetodoPago import MetodoPago
from backend.Modelos.database import db

# Función para actualizar un método de pago existente
def update_metodo_pago():
    print("Contenido de la sesión:", session)

    id_usuario = session.get('user')
    if not id_usuario:
        print("No hay id_usuario en la sesión, redirigiendo al login...")
        return redirect(url_for('login'))

    if request.method == 'POST':
        id_metodo = request.form.get('id')
        tipo = request.form.get('tipo')
        tarjeta = request.form.get('tarjeta')
        fecha_caducidad = request.form.get('fecha_caducidad')
        csv = request.form.get('csv')

        metodo = MetodoPago.query.filter_by(id_metodo=id_metodo, id_usuario=id_usuario).first()

        if not metodo:
            print("Método de pago no encontrado para editar.")
            return redirect(url_for('metodos_pago'))

        metodo.tipo = tipo
        metodo.tarjeta = tarjeta
        metodo.fecha_caducidad = fecha_caducidad
        metodo.csv = csv
        metodo.updated_at = datetime.datetime.now()

        db.session.commit()
        
    return redirect(url_for('metodos_pago'))
