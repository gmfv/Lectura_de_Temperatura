from smbus2 import SMBus
from mlx90614 import MLX90614
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

push= #pin GPIO del boton
GPIO.setup(push, GPIO.IN)

def lectura_boton():
    if GPIO.input(push):
        return False
    else:
        return True

while True:
    #Se establece la comunicacion con el sensor
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    #Se cargan los datos leidos por el sensor
    boton=lectura_boton()
    if boton is True:
        print sensor.get_amb_temp()
        print sensor.get_obj_temp()
        boton=False
    sleep(0.1)
    bus.close()
