from backend.Modelos.database import db
from sqlalchemy.orm import relationship
import datetime

class MetodoPago(db.Model):
    __tablename__ = 'metodos_pago'

    id_metodo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    tarjeta = db.Column(db.String(20), nullable=False)
    fecha_caducidad = db.Column(db.Date, nullable=False)
    csv = db.Column(db.String(4), nullable=False)

    tipo = db.Column(db.Enum('tarjeta', 'paypal', 'otro', name='tipo_metodo'), nullable=False, default='tarjeta')

    is_default = db.Column(db.Boolean, nullable=False, default=False)

    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    usuario = relationship('Usuario', back_populates='metodos_pago')
