from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Rioazulq12@localhost/comercial'
db = SQLAlchemy(app)


class clientes(db.Model):
    codigo = db.Column(db.String(5), unique=True, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)


db.create_all()


@app.route('/')
def index():
    clien = clientes.query.all() # todo select * from clientes
    return render_template("listado.html",misclientes=clien)


app.run(debug=True)
