import os
from flask import Flask
from backend.Modelos.database import init_db
from routes.home import home
from routes.authentication import *
from dotenv import load_dotenv
from routes.user import informacion_personal

from routes.usuario.compras import compras

from routes.usuario.metodos_de_pago import *


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Para el login
app.secret_key = os.urandom(24)  

# Configuración del correo utilizando variables de entorno
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Inicializar la base de datos
init_db(app)

# Definir las rutas
app.add_url_rule('/', 'home', home)
app.add_url_rule('/login', 'login', login, methods=["GET", "POST"])
app.add_url_rule('/registro', 'registro', registro, methods=["GET", "POST"])
app.add_url_rule('/olvidado_contraseña', 'olvidado_contraseña', olvidado_contraseña, methods=["GET", "POST"])
app.add_url_rule('/restablecer_contraseña/<token>', 'restablecer_contraseña', restablecer_contraseña, methods=["GET", "POST"])
app.add_url_rule('/informacion_personal', 'informacion_personal', informacion_personal)
app.add_url_rule('/update_usuario', 'update_usuario', update_usuario, methods=['POST']) 
app.add_url_rule('/compras', 'compras', compras, methods=["GET", "POST"])
app.add_url_rule('/cambiar_contraseña', 'cambiar_contraseña', update_contraseña, methods=["GET", "POST"])

app.add_url_rule('/cerrar_sesion', 'cerrar_sesion', cerrar_sesion, methods=["GET", "POST"])


app.add_url_rule('/metodos_pago','metodos_pago', metodos_pago, methods=["GET" , "POST"])
app.add_url_rule('/add_metodo_pago','add_metodo_pago', add_metodo_pago, methods=["GET" , "POST"])
app.add_url_rule('/update_metodo_pago', 'update_metodo_pago', update_metodo_pago, methods=["POST"])
app.add_url_rule('/delete_metodo_pago/<int:id_metodo>', 'delete_metodo_pago', delete_metodo_pago, methods=["POST"])

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
