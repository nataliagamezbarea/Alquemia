from backend.Modelos.database import db 

class Producto(db.Model):
    __tablename__ = 'productos'

    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo_producto = db.Column(db.Enum('chico', 'chica', 'unisex'), nullable=False)

    imagenes = db.relationship('ProductoImagen', backref='producto')
    variantes = db.relationship('ProductoVariante', backref='producto')
    categorias = db.relationship('Categoria', secondary='producto_categoria', backref='productos')
