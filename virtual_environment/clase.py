import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
cosa = Flask(__name__)

paises = [{'Nombre':'Colombia', 'Capital':'Bogota', 'Bandera': '../colombia.jpg'},
          {'Nombre':'Tailandia', 'Capital':'Monkog', 'Bandera': 'tailandia.jpg'},
          {'Nombre':'Holanda', 'Capital':'Amsterdam', 'Bandera': 'holanda.png'},
          {'Nombre':'Republica del congo', 'Capital':'Brazzaville', 'Bandera': 'republica_del_congo.jpg'}]

@cosa.route('/')
def mostrar_paises():
    return render_template('paises.html', paises = paises)

if __name__ == '__main__':
    cosa.run()

