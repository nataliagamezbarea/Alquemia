from backend.Modelos.database import db 
from sqlalchemy.orm import relationship

class PedidoProducto(db.Model):
    __tablename__ = 'pedido_productos'

    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), primary_key=True, nullable=False)
    id_variantes = db.Column(db.Integer, db.ForeignKey('producto_variantes.id_variantes'), primary_key=True, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=1)


    variantes = relationship('ProductoVariante', backref='pedido_productos', lazy=True)
