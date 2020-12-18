from app import db

class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column(db.Integer, primary_key=True )
    nome = db.Column(db.string())

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome
        }

