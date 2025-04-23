from backend.Modelos.database import db 

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoria_nombre = db.Column(db.String(100), nullable=False)
