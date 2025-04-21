import datetime
from flask import render_template, request, session, redirect, url_for
from backend.Modelos.MetodoPago import MetodoPago
from backend.Modelos.database import db

# Función para manejar la visualización de los métodos de pago
def metodos_pago():
    # Verificar el contenido de la sesión
    print("Contenido de la sesión:", session)

    # Obtener el id_usuario de la sesión utilizando la clave "user"
    id_usuario = session.get('user')  # Usamos 'user' en vez de 'user_id'
    
    # Comprobar si el id_usuario existe
    if not id_usuario:
        print("No hay id_usuario en la sesión, redirigiendo al login...")
        return redirect(url_for('login'))  # Redirige a la página de login si no hay id_usuario
    
    # Obtener los métodos de pago del usuario
    metodos = MetodoPago.query.filter_by(id_usuario=id_usuario).all()

    # Renderiza la página con los métodos de pago
    return render_template('user/usuario_configuracion/metodos_pago/metodos_pago.html', metodos=metodos)

