from flask import  Flask
from crud_clientes.app.config import Config
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import  Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)



from crud_clientes.app import  routes,models





