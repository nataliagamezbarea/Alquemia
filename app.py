import os
from flask import Flask
from backend.Modelos.database import init_db
from routes.home import home
from routes.registro import registro
from routes.login import login

app = Flask(__name__)

# Para el login 
app.secret_key = os.urandom(24)


init_db(app)

app.add_url_rule('/', 'home', home)
app.add_url_rule('/login', 'login', login, methods=["GET", "POST"])
app.add_url_rule('/registro', 'registro', registro, methods=["GET", "POST"])


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
