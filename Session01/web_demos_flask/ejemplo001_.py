from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #todo contexto
    context = {
        "curso": "Flask",
        "hora": 20,
        "tecnologia": "Web,Microservicios",
        "profesor": "Armando Ruiz",
    }
    return render_template("index.html", info=context)


@app.route('/quienes')
def quienes():
    return render_template("quienes.html")


#app.run("0.0.0.0",debug=True,port=8000)
app.run(debug=True,port=8000)
