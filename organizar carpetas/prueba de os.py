import os
from datetime import datetime
import locale
import shutil


ruta = os.path.join('C:/Users/Usuario/Documents/1-LUIS/1-Programacion/5-Automatizaciones python','dataset')

os.mkdir("dataset")

shutil.move('pruebaMover.py',ruta)


