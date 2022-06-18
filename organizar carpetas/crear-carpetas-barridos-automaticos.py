import os
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es-ES')

#ruta de doden esta hay que programarla

fecha_actual = datetime.now()

fechaActualf= datetime.strftime(fecha_actual,"%d-%m-%Y")

fechaActualm= datetime.strftime(fecha_actual,"%B-%Y")

mes=fechaActualm.capitalize()
#if de si existe
os.mkdir(mes)

with open('Rendimiento Diario '+fechaActualf+'.xlsx','w') as f:
    f.close

#mover archivo redimiento a mes ruta o siendo consecuentes copio archivo y renombro externo e internamente
