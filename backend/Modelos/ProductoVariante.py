from backend.Modelos.database import db
from backend.Modelos.Color import Color
from backend.Modelos.Producto import Producto

class ProductoVariante(db.Model):
    __tablename__ = 'producto_variantes'

    id_variantes = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('colores.id_color'), nullable=False)
    talla = db.Column(db.String(10))
    stock = db.Column(db.Integer, nullable=False, default=0)

    producto = db.relationship('Producto', back_populates='variantes')
    # Este backref ya está correctamente configurado
    color = db.relationship('Color', backref='producto_variantes_color')
