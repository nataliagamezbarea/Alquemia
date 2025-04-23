from backend.Modelos.database import db

class Producto(db.Model):
    __tablename__ = 'productos'

    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo_producto = db.Column(db.Enum('hombre', 'mujer'), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    imagenes = db.relationship('ProductoColorImg', backref='producto_imagen', lazy=True)  
    variantes = db.relationship('ProductoVariante', back_populates='producto')
    categorias = db.relationship('Categoria', secondary='producto_categoria', backref='productos')
