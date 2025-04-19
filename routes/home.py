from flask import render_template, session

def home():
    if "user" in session:
        # Verificar si es administrador usando la variable de sesión directamente
        if "is_admin" in session and session["is_admin"]:
            return render_template("admin/admin.html")  # Redirigir a la página de admin
        return render_template("user/usuario_configuracion/user.html")  # Redirigir a la página de usuario
    return render_template("user/home.html")
