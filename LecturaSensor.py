from smbus2 import SMBus
from mlx90614 import MLX90614
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) #Usa la numeracion fisica

push= 10 #pin GPIO del boton
GPIO.setup(push, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def lectura_boton():
    if GPIO.input(push):    
	    print "Boton presionado" 	
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
        print "Temperatura Ambiente : ", sensor.get_ambient()
        print "Temperatura de Objeto: ", sensor.get_object_1()
        boton=False
    sleep(0.3)
    bus.close()
