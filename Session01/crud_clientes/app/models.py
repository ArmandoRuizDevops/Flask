from crud_clientes.app import  db

class Customers(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60))
    state = db.Column(db.String(5))