from flask import render_template, request, session
from backend.Modelos.Usuario import Usuario
import bcrypt

def login():
    # Si el usuario ya ha iniciado sesión
    if "user" in session:
        # Verificar si es administrador usando la variable de sesión directamente
        if "is_admin" in session and session["is_admin"]:
            return render_template("admin/admin.html")  # Redirigir a la página de admin
        return render_template("user/usuario_configuracion/user.html")  # Redirigir a la página de usuario

    # Si es un POST (cuando se envían las credenciales)
    if request.method == "POST":
        email = request.form["email"]
        contrasena = request.form["contrasena"]

        # Buscar el usuario en la base de datos y verificar la contraseña
        usuario_encontrado = Usuario.query.filter_by(email=email).first()
        if usuario_encontrado and bcrypt.checkpw(contrasena.encode("utf-8"), usuario_encontrado.contrasena.encode("utf-8")):
            session["user"] = usuario_encontrado.id_usuario
            session["is_admin"] = usuario_encontrado.is_admin
            # Redirigir a la página correspondiente según el rol
            if usuario_encontrado.is_admin:
                return render_template("admin/admin.html")  # Si es admin, redirigir a la página de admin
            return render_template("user/usuario_configuracion/user.html")  # Si no es admin, redirigir a la página de usuario

        # Si las credenciales son incorrectas
        return render_template("authentication/login.html", error="Credenciales incorrectas")

    # Si no es un POST, renderizar el formulario de login
    return render_template("authentication/login.html")
