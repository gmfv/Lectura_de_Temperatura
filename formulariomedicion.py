import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from datetime import datetime, date, time

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
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Ingrese su cédula, seleccione medir y luego confirmar")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Cédula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedulacarga=tk.StringVar()
        self.entrycedula=ttk.Entry(self.labelframe1, textvariable=self.cedulacarga)
        self.entrycedula.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Medición:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.medicioncarga=tk.StringVar()
        self.entrymedicion=ttk.Entry(self.labelframe1, textvariable=self.medicioncarga)
        self.entrymedicion.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe1, text="Medir", command=self.agregar)
        self.boton2.grid(column=2, row=2, padx=4, pady=4)

    
    def agregar(self):
        #datos=(self.medicioncarga.get(), self.cedulacarga.get())
        hora=datetime.time(datetime.now())
        datos = (self.medicioncarga.get(), self.cedulacarga.get(), date.today(), hora)
        #print (datos)
        self.medicion1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.medicioncarga.set("")
        self.cedulacarga.set("")

    def agregar_f(self):
        datos=(self.cedulacargaf.get(), self.nombrecarga.get())
        self.medicion1.alta_f(datos)
        mb.showinfo("Información", "Funcionario agregado")
        self.cedulacarga.set("")
        self.nombrecarga.set("")

    def consulta_por_cedula(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por cédula")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Ingrese la cédula del funcionario")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Cédula:")
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
        #print(respuesta)
        if len(respuesta)>0:
            
            self.scrolledtext2.delete("1.0", tk.END)        
            for row in respuesta:
                self.scrolledtext2.insert(tk.END, "Temperatura: "+str(row[0])+"\nFecha: "+str(row[1])+"\Hora: "+str(row[3])+"\n\n")
        else:
            self.cedula.set('')
            mb.showinfo("Información", "No existe registro del funcionario")

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
            self.scrolledtext1.insert(tk.END, "Cédula:"+str(row[0])+"\n Nombre:"+row[1]+"\n\n")

    def carga_funcionario(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Cargar funcionario")
        self.labelframe3=ttk.LabelFrame(self.pagina4, text="Agregar datos del funcionario nuevo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe3, text="Cédula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedulacargaf=tk.StringVar()
        self.entrycedula=ttk.Entry(self.labelframe3, textvariable=self.cedulacargaf)
        self.entrycedula.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe3, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombrecarga=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe3, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe3, text="Agregar", command=self.agregar_f)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

aplicacion1=FormularioMedicion()