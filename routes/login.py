from flask import render_template, request, session
from backend.Modelos.Usuario import Usuario
import bcrypt

def login():
    # Si el usuario ya ha iniciado sesión, se dirige a la página correspondiente
    if "user" in session:
        # Verificar si es un usuario administrador
        if session.get("is_admin"):
            return render_template("admin/admin.html")  # Redirigir a la página de administrador
        return render_template("user/usuario_configuracion/user.html")  # Redirigir a la página de usuario normal

    if request.method == "POST":
        # Obtener los datos del formulario
        email = request.form["email"]
        contrasena = request.form["contrasena"]

        # Buscar el usuario en la base de datos por su email
        usuario_encontrado = Usuario.query.filter_by(email=email).first()

        # Verificar si el usuario existe y si la contraseña es correcta
        if usuario_encontrado and bcrypt.checkpw(contrasena.encode("utf-8"), usuario_encontrado.contrasena.encode("utf-8")):
            # Si la contraseña es válida, guardar los datos del usuario en la sesión
            session["user"] = usuario_encontrado.id_usuario
            session["is_admin"] = usuario_encontrado.is_admin  # Guardar si es administrador o no
            # Redirigir a la página correspondiente dependiendo del tipo de usuario
            if usuario_encontrado.is_admin:
                return render_template("admin/admin.html")  # Si es admin, redirigir a la página de admin
            return render_template("user/usuario_configuracion/user.html")  # Si no es admin, redirigir a la página de usuario

        # Si las credenciales no son correctas, mostrar un mensaje de error
        return render_template("authentication/login.html", error="Credenciales incorrectas")

    # Si no se ha hecho un POST, simplemente renderizar el formulario de login
    return render_template("authentication/login.html")
