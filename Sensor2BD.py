from smbus2 import SMBus
from mlx90614 import MLX90614
import RPi.GPIO as GPIO
from time import sleep
from datetime import date, datetime
import mariadb 

conn = mariadb.connect(
    user="root",
    password="",
    host="localhost",
    database="AplicacionSensorTemperatura")
cur = conn.cursor() 

GPIO.setmode(GPIO.BOARD)

push= 10 
GPIO.setup(push, GPIO.IN)

def lectura_boton():
    if GPIO.input(push):
        return False
    else:
        return True

while True:
    #Se establece la comunicacion con el sensor
    bus = SMBus(1)
    dir= 0x5A #pin GPIO del sensor
    sensor = MLX90614(bus, address=dir)
    #Se cargan los datos leidos por el sensor
    ced = int(input("Ingrese su número de cédula: "))
    boton=lectura_boton()
    if boton is True:
        tempe= sensor.get_obj_temp()
        boton=False
    sleep(0.1)
    bus.close()
    today = date.today()
    now= = datetime.now()
    d1= today.strftime("%d/%m/%Y")
    d2=now.strftime("%H:%M:%S")
    id_medicion="1"
    lugar_marcacion="Ala norte"
    try:
        cur.execute("INSERT INTO Medicion values((?), (?), (?), (?), (?), (?))", (id_medicion, tempe, cedulafuncionario, d1, hora, lugar_marcacion))
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit()     
    conn.close()