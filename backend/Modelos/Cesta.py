from backend.Modelos.database import db 

class Cesta(db.Model):
    __tablename__ = 'cesta'

    id_cesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    productos = db.relationship('ProductoVariante', secondary='cesta_productos', backref='cestas')
