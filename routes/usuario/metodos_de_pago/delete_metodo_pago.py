import datetime
from flask import render_template, request, session, redirect, url_for
from backend.Modelos.MetodoPago import MetodoPago
from backend.Modelos.database import db


def delete_metodo_pago(id_metodo):

    id_usuario = session.get('user')  
    
    # Comprobar si el id_usuario existe
    if not id_usuario:
        return redirect(url_for('login'))  
    
    # Obtener el método de pago que se quiere eliminar
    metodo = MetodoPago.query.filter_by(id_metodo=id_metodo, id_usuario=id_usuario).first()
    
    # Si el método no existe, redirigir
    if not metodo:
        print("Método de pago no encontrado.")
        return redirect(url_for('metodos_pago'))

    db.session.delete(metodo)
    db.session.commit()
   
    
    # Si todo va bien, redirige a la página de métodos de pago para mostrar los métodos actualizados
    return redirect(url_for('metodos_pago'))
