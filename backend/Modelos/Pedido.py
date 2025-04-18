from backend.Modelos.database import db 

class Pedido(db.Model):
    __tablename__ = 'pedido'

    id_pedido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido1 = db.Column(db.String(50), nullable=False)
    apellido2 = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50))
    tipo_pedido = db.Column(db.String(50))
    fecha = db.Column(db.Date, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    productos = db.relationship('ProductoVariante', secondary='pedido_productos', backref='pedidos')
    tiendas = db.relationship('Tienda', secondary='pedido_tienda', backref='pedidos')
    detalles = db.relationship('DetallesPedido', uselist=False, backref='pedido')
