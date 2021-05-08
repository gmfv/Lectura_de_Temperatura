import os
import sqlite3
from sqlite3 import Error
import time
import json

def sql_connection():
    try:
        conn = sqlite3.connect('Base_Datos/Sonda_Abril.db')
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE lecturas(id integer PRIMARY KEY AUTOINCREMENT, datatime integer, Temperatura integer, pH integer)")
    conn.commit()

def sql_insert(conn, lecturas):
    cur = conn.cursor()
    cur.execute("INSERT INTO lecturas(datatime, Temperatura,pH,DO) VALUES(datetime('now', 'localtime'),?,?,?)"", lecturas)

conn = sql_connection()

try:
    sql_table(conn)
except Error:
    pass

c = conn.cursor()


def valDate(dateAct, dateAnt, tol):
    global aux
    aux = False
    if (dateAct < (dateAnt + tol) and dateAct > (dateAnt - tol)):
        aux = False
        return dateAct
    else:
        aux = True
        return dateAnt

def sensorRead():
    #Aca se leen los sensores
    #apagar el sensor
    lect=(temp,PH,DO,CE...)
    return lect

while True:

    sensorRead()

    sql_insert(conn, sensorRead()) #Aca podria ser lect creo
    time.sleep(tiempo)
