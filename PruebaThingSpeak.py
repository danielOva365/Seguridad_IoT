#Prueba de ThingSpeak
import requests
import json


#Librerias proyecto
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep 

#Librerias para git
from git import Repo

PATH_OF_GIT_REPO = '/home/pi/Desktop/Seguridad_git/Seguridad_IoT'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'Prueba desde python'

def git_push():
    try:
        
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        print("1")
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    


def main():
    #URL para el envío de datos al canal
    #urlBase = "https://api.thingspeak.com/update?api_key=29A7ELQWULOJBN7N"
    urlBase= "https://api.thingspeak.com/update?api_key=V2PO23F3KW69VPQT"   #URL de nuestro canal

    #Asignar variables (equivalente a leer los sensores)
    movimiento_pir = 1
    camara = 21.8
    presion = 1

    #Antes de enviar armamos el string que contiene la URL completa con los datos
    dataString = urlBase + "&field1=" + str(movimiento_pir)
    dataString2 = urlBase + "&field2=" + str(camara) + "&field3=" + str(presion)


    #Enviamos el string para escribir un conjunto de datos en cada campo
    respuesta = requests.get(dataString)
    #respuesta2 =  requests.get(dataString2)

    #Imprimir la respuesta, que es el identificador de los datos enviados (contador)
    print(respuesta.text)

    #Enviar petición para leer el feed de los últimos 5 datos enviados de todos los campos (2 campos: temperatura y humedad)
    respuesta = requests.get("https://api.thingspeak.com/channels/1686207/feeds.json?api_key=V0PITGZBU92NIH0V&results=2")
    print(respuesta.text)

    #Convertir la respuesta recibida que se encuentra en formato JSON, a formato de diccionario de Python
    datos = json.loads(respuesta.text)
    print(datos)

    '''
    #Imprimir el primer dato de temperatura, de los cinco que se solicitaron
    pirleido = datos["feeds"][0]["field1"]
    print(pirleido)
    #Imprimir el tercer dato de humedad, de los cinco que se solicitaron
    presionleida = datos["feeds"][2]["field2"]
    print(presionleida)'''

    #Imprimir los cinco datos de temperatura
    '''print("Los 2 datos de presion")
    for i in range(5):
        tempLeida = datos["feeds"][i]["field1"]
        print(tempLeida) '''

    #Petición para leer los cinco últimos datos del campo 1 (field1 = temperatura)
    '''respuesta = requests.get("https://api.thingspeak.com/channels/115470/fields/1.json?api_key=383NBO2ANDYSI6HN&results=5")
    print(respuesta.text)
    '''

git_push()
