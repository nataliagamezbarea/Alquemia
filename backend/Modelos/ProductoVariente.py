from backend.Modelos.database import db 

class ProductoVariante(db.Model):
    __tablename__ = 'producto_variantes'

    id_variantes = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    color = db.Column(db.String(50))
    talla = db.Column(db.String(10))
    stock = db.Column(db.Integer, nullable=False, default=0)
