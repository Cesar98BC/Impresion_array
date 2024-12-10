
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    nombre="Cesar Briones"
    Licenciaturas=["ISC","ID","ARQ"]
    return render_template('index.html',nombre=nombre,Licenciaturas=Licenciaturas,len=len(Licenciaturas))