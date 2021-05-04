/*
 * Diego Valenzuela - Ing. Mecatronica.
 */
package controlador;
import java.sql.*; 


/**
 *
 * @author Diego
 */
public class Conexion {
    private String nombreBD="SensorTemperatura1";
    private String url="jdbc:mysql://127.0.0.1"+ nombreBD;
    private String usuario="root";
    private String pass="";        
    private Connection con; //dentro del paquete java.sql.*
    
    public Conexion(){ //constructor de la clase
        try{
            Class.forName("orq.gjt.mm.mysql.Driver");
            con=DriverManager.getConnection(url,usuario,pass);
        }
        catch(ClassNotFoundException | SQLException e){
            System.out.println("No se pudo conectar correctamente a la Base de Datos");
        }
    }
    public Connection Conectar(){
        return con; // con nos deja hacer nuestras consultas
    }
}
