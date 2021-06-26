import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from datetime import datetime, date, time
from smbus2 import SMBus
from mlx90614 import MLX90614
import RPi.GPIO as GPIO

import medicion

class FormularioMedicion:
    def __init__(self):
        self.medicion1=medicion.Medicion()
        self.ventana1=tk.Tk()
        self.ventana1.title("Control de temperatura")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_medicion()
        self.carga_funcionario()
        self.consulta_por_cedula()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_medicion(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de medicion")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Ingrese su cedula, seleccione medir y luego confirmar")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Cedula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedulacarga=tk.StringVar()
        self.entrycedula=ttk.Entry(self.labelframe1, textvariable=self.cedulacarga)
        self.entrycedula.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Medicion:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.medicioncarga=tk.StringVar()
        self.entrymedicion=ttk.Entry(self.labelframe1, textvariable=self.medicioncarga, state="readonly")
        self.entrymedicion.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Medir", command=self.medir)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton2.grid(column=2, row=2, padx=4, pady=4)

    def medir(self):
        bus = SMBus(1)
        dir= 0x5A #pin GPIO del sensor
        sensor = MLX90614(bus, address=dir)
        tempe= round(sensor.get_object_1(),2)+3
        bus.close()
        self.entrymedicion.configure(state='normal')
        self.medicioncarga.set("")
        self.entrymedicion.insert(0,str(tempe))
        self.entrymedicion.configure(state='disabled')

    def agregar(self):
        hora=datetime.now().strftime("%H:%M:%S")
        datos = (self.medicioncarga.get(), self.cedulacarga.get(), date.today(), hora, "Ala Norte")
        respuesta = self.medicion1.consultaexistencia(self.cedulacarga.get())
        if len(respuesta)>0:
            self.medicion1.alta(datos)
            mb.showinfo("Informacion", "Los datos fueron cargados")
        else:
            mb.showinfo("Informacion", "No existe registro del funcionario")
        self.medicioncarga.set("")
        self.cedulacarga.set("")

    def agregar_f(self):
        datos=(self.cedulacargaf.get(), self.nombrecarga.get(), self.correocargaf.get(), self.telefonocarga.get())
        respuesta = self.medicion1.consultaexistencia(self.cedulacargaf.get())
        if len(respuesta)>0:
            mb.showinfo("Informacion", "Ya existe registro del funcionario")
        else:
            self.medicion1.alta_f(datos)
            mb.showinfo("Informacion", "Funcionario agregado")    
        self.cedulacargaf.set("")
        self.nombrecarga.set("")
        self.correocargaf.set("")
        self.telefonocarga.set("")

    def consulta_por_cedula(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por cedula")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Ingrese la cedula del funcionario")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Cedula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedula=tk.StringVar()
        self.entrycedula=ttk.Entry(self.labelframe2, textvariable=self.cedula)
        self.entrycedula.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.scrolledtext2=st.ScrolledText(self.labelframe2, width=30, height=10)
        self.scrolledtext2.grid(column=0,row=1, padx=10, pady=10)
        #self.scrolledtext2.configure(state ='disabled')

    def consultar(self):
        datos=(self.cedula.get())
        respuesta=self.medicion1.consulta(datos)
        if len(respuesta)>0:
            self.scrolledtext2.delete("1.0", tk.END)        
            for row in respuesta:
                self.scrolledtext2.insert(tk.END, "Temperatura: "+str(row[0])+"\nFecha: "+str(row[1])+"\nHora: "+str(row[2])+"\nLugar de Marcación: "+str(row[3])+"\n\n")
        else:
            self.cedula.set('')
            mb.showinfo("Informacion", "No existe registro del funcionario")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Funcionarios")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.medicion1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for row in respuesta:
            self.scrolledtext1.insert(tk.END, "Cedula:"+str(row[0])+"\n Nombre:"+row[1]+"\n Correo:"+row[2]+"\n Telefono:"+row[3]+"\n\n")

    def carga_funcionario(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Cargar funcionario")
        self.labelframe3=ttk.LabelFrame(self.pagina4, text="Agregar datos del funcionario nuevo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe3, text="Cedula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedulacargaf=tk.StringVar()
        self.entrycedula=ttk.Entry(self.labelframe3, textvariable=self.cedulacargaf)
        self.entrycedula.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe3, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombrecarga=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe3, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe3, text="Correo:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.correocargaf=tk.StringVar()
        self.entrycorreo=ttk.Entry(self.labelframe3, textvariable=self.correocargaf)
        self.entrycorreo.grid(column=1, row=3, padx=4, pady=4)
        self.telefonocarga=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe3, textvariable=self.telefonocarga)
        self.entrytelefono.grid(column=1, row=4, padx=4, pady=4)
        self.label4=ttk.Label(self.labelframe3, text="Telefono:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe3, text="Agregar", command=self.agregar_f)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

aplicacion1=FormularioMedicion()