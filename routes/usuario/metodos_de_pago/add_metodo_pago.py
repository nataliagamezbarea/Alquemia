import datetime
from flask import render_template, request, session, redirect, url_for
from backend.Modelos.MetodoPago import MetodoPago
from backend.Modelos.database import db


def add_metodo_pago():

    id_usuario = session.get('user') 
    
    if request.method == 'POST':
        tipo = request.form['tipo']
        tarjeta = request.form.get('tarjeta', '')
        fecha_caducidad = request.form['fecha_caducidad']
        csv = request.form.get('csv', '')
        is_default = 'is_default' in request.form

        # Obtener la fecha y hora actual para updated_at
        updated_at = datetime.datetime.now()

        nuevo_metodo = MetodoPago(
            id_usuario=id_usuario,
            tipo=tipo,
            tarjeta=tarjeta,
            fecha_caducidad=fecha_caducidad,
            csv=csv,
            is_default=is_default,
            updated_at=updated_at  
        )
        
        db.session.add(nuevo_metodo)
        db.session.commit()
        
        return redirect(url_for('metodos_pago'))  


