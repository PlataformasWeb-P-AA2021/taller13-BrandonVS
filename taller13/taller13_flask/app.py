from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
                     auth=('brandon', '12345'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
                           numero_edificios=numero_edificios)


@app.route("/losdepartamentosdos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
                     auth=('user', 'pass'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombre_prop': d['nombre_prop'], 'costo': d['costo'], 'cuartos': d['cuartos'], 
                       'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2,
                           numero=numero)


# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('brandon', '12345'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
