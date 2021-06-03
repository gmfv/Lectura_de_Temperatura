import mysql.connector
class Medicion:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="sensortemperatura1")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        #sql="insert into medicion(temperatura, cedula_f) values (%s,%s)"
        sql="insert into medicion(temperatura, cedula_f, fecha, hora) values (%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def alta_f(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into funcionario(cedula, nombre) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select temperatura, fecha, hora from medicion where cedula_f = '%s'" % datos
        #print (sql)
        cursor.execute(sql)
        registro=cursor.fetchall()
        cone.close()
        #print(cursor.fetchall())
        return registro

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select cedula, nombre from funcionario"
        cursor.execute(sql)
        registro=cursor.fetchall()
        cone.close()
        return registro
