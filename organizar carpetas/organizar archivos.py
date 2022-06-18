import os
import sys
import shutil
import time 



# ruta_instaladores = "C:\Users\Usuario\Downloads\Instaladores"
# ruta_exli = "C:\Users\Usuario\Downloads\excel y libreoffice"
# ruta_img = "C:\Users\Usuario\Downloads\Imagenes"
# ruta_video = "C:\Users\Usuario\Downloads\videos"
ruta_descargas = os.getcwd()

temporizador = 30
#aui tengo que hacer un listdir

ext_vid = ['.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv']
ext_aud = ['.mp3', '.wma', '.wav', '.flac']
ext_img = ['.jpg', '.png', 'jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg']
ext_doc = ['.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf',".xls","xlsk"]
ext_com = ['.zip', '.rar', '.rar5', '.7z', '.ace', '.gz']
ext_ins = ['.exe', '.msi']

ext = ''
archivo = ''

def RD(extv,nfolder):

    if ext in extv:
        shutil.move(ruta_descargas + archivo, ruta_descargas + nfolder)

    
    if ext != '':
        shutil.move(ruta_descargas + archivo, ruta_descargas + extv)

#tienes que poer las rutas
def ordenar(archivo, ext):
        RD(ext_doc,"Documentos")
        RD(ext_vid,"Videos")
        RD(ext_aud,"Audio")
        RD(ext_img,"Imagenes")
        RD(ext_doc,"Documentos")
        RD(ext_ins,'Instaladores')
        RD(ext_com,'Comprimidos')
        RD('','Otros')
#declarar que es ext


def verificar():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar(nombre_archivo, ext)

verificar()
""" 
while(True):
    try:
        time.sleep(temporizador)
        for _ in range(len(os.listdir(ruta_descargas))):
            try:
                verificar()
            except:
                pass
    except KeyboardInterrupt:
        break """