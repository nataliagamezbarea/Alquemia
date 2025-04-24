from backend.Modelos.database import db
from backend.Modelos.ProductoImagen import ProductoImagen


class Producto(db.Model):
    __tablename__ = 'productos'

    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    # Relaciones
    variantes = db.relationship('ProductoVariante', back_populates='producto')
    imagenes = db.relationship('ProductoImagen', back_populates='producto')
