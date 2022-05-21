from flask import render_template
from crud_clientes.app import app, db
from crud_clientes.app.models import Customers


@app.route('/')
def index():
    clientes = Customers.query.all()
    return render_template("index.html", clientes=clientes)
