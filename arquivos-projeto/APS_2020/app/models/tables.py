from app import db

class Noticia(db.Model):
    __tablename__ = "noticias"

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, unique=True)
    titulo = db.Column(db.String)
    data = db.Column(db.String)

    def __init__(self, link, titulo, data):
        self.link = link
        self.titulo = titulo
        self.data = data

    def __repr__(self):
        return "<Noticia: %r>" % self.link


