from backend.Modelos.database import db

class Color(db.Model):
    __tablename__ = 'colores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color_nombre = db.Column(db.String(100), nullable=False)
    