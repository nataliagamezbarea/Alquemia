from flask import render_template, request, session
from backend.Modelos.Usuario import Usuario
import bcrypt


def login():

    # Si el usuario ha iniciado sessión 
    if "user" in session:
        return render_template("user/usuario_configuracion/user.html")
    if "is_admin" in session:
        return render_template("admin/admin.html")

    if request.method == "POST":
        email = request.form["email"]
        contrasena = request.form["contrasena"]

        usuario_encontrado = Usuario.query.filter_by(email=email).first()

        # Si el usuario coincide con la contraseña hasheada vas a guardar el usuario y si es admin
        if usuario_encontrado and bcrypt.checkpw(contrasena.encode("utf-8"), usuario_encontrado.contrasena.encode("utf-8")):
            session["user"] = usuario_encontrado.id_usuario
            session["is_admin"] = usuario_encontrado.is_admin
            return render_template("user/usuario_configuracion/user.html")

        return render_template("authentication/login.html", error="Credenciales incorrectas")

    return render_template("authentication/login.html")
