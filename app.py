from flask import Flask
from backend.Modelos.database import init_db
from routes.home import home

app = Flask(__name__)


init_db(app)

app.add_url_rule('/', 'home', home)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
