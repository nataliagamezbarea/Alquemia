from backend.Modelos.database import db

class Color(db.Model):
    __tablename__ = 'colores'

    id_color = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color_nombre = db.Column(db.String(100), nullable=False)
    img_color = db.Column(db.Text)

    producto_variantes = db.relationship('ProductoVariante', backref='producto_variantes_color')
