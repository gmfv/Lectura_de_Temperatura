import MySQLdb
from datetime import datetime
from smbus2 import SMBus
from mlx90614 import MLX90614
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD) #Usa la numeracion fisica

push= 10 #pin GPIO del boton
GPIO.setup(push, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#elementos para obtener la fecha y la hora
now=datetime.now()


def lectura_boton():
    if GPIO.input(push):    
	    print ("Boton presionado") 	
	    return True	
    else:
        return False

while True:
    #Se establece la comunicacion con el sensor
    bus = SMBus(1)
    dir= 0x5A # GPIO del sensor
    sensor = MLX90614(bus, address=dir)
    #Se cargan los datos leidos por el sensor
    boton=lectura_boton()
    if boton is True:
        print ("Temperatura Ambiente : ", sensor.get_ambient())
        print ("Temperatura de Objeto: ", sensor.get_object_1())
        temperatura=sensor.get_object_1()
        fecha=now.date()
        hora=now.time()
        lugar="EntradaPrincipal"
        cedula="1234567" #este es el problema, debe de obtener de la base de datos
        idmedicion="1"
        miConexion=MySQLdb.connect(host="",user="root",passwd="",db="lecturatemperatura")
        cur=miConexion.cursor()
        cur.execute("INSERT into medicion (id_medicion,temperatura,cedulafuncionario,fecha,hora,lugar_medicion) values + (",idmedicion,",",temperatura,",",cedula,",",fecha,",",hora,",",lugar,")")
        miConexion.close()
        boton=False
    sleep(0.3)

    bus.close()