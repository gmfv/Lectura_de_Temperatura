/*
 * Diego Valenzuela - Ingenieria Mecatronica
 */
package modelo;
import controlador.Conexion;
import java.sql.*; // contiene al objeto connection
import java.util.*; //contiene la libreria LIST 

/**
 *
 * @author Diego
 */
public class MedicionDAO {
    private Conexion c = new Conexion();
    private Connection con;
    private PreparedStatement ps; 
    private ResultSet rs; 
    
    public MedicionDAO(){
        
    }
    
    //1- Listar
    public List<Medicion> listar(){
        ArrayList <Medicion> lista = new ArrayList();
        String sql="SELECT * FROM medicion";
        try{
            con = c.Conectar(); // me conecto con la base de datos
            ps= con.prepareStatement(sql); 
            rs= ps.executeQuery(); //lista de registros que voy a ir recuperando
            while(rs.next()){
                Medicion m= new Medicion();
                m.setTemperatura(rs.getFloat("id_medicion"));
                m.setTemperatura(rs.getFloat("temperatura"));
                m.setCedulaFuncionario(rs.getString("cedulafuncionario"));
                m.setFecha(rs.getString("fecha"));
                m.setHora(rs.getString("hora"));
                m.setLugarMarcacion(rs.getString("lugar_marcacion"));
                lista.add(m);
            }
            
        }
        catch(Exception e){
            System.out.println("NO se pudo LISTAR las MEDICIONES");
        }
        return lista;
    }
    //2- Agregar un nuevo elemento
    public boolean insetar(Medicion m){
        boolean r=false;
        String sql="INSERT INTO medicion (id_medicion, temperatura,cedulafuncionario,fecha,hora,lugar_marcacion)"+"VALUES(?,?,?,?,?,?)";
        try{
            con=c.Conectar();
            ps=con.prepareStatement(sql);
            ps.setString(1,m.getIDMedicion());
            ps.setFloat(2,m.getTemperatura());
            ps.setString(3,m.getCedulaFuncionario());
            ps.setString(4,m.getFecha());
            ps.setString(5,m.getHora());
            ps.setString(6,m.getLugarMarcacion());
            int resultado=ps.executeUpdate();
            if(resultado==0){
                r=true;
            }
        }
        catch(Exception e){
            System.out.println("NO se pudo AGREGAR el nuevo elemento en MEDICION");
        }
        return r;
    }
    //3- Eliminar un elemento
    public boolean eliminar(String id){ //c es numero de cedula
        boolean r=false;
        String sql="DELETE FROM funcionario WHERE id_medicion="+id;
        try{
            con= c.Conectar();
            ps=con.prepareStatement(sql);
            int resultado=ps.executeUpdate();
            if(resultado==0){
                r=true;
            }
        }
        catch(Exception e){
            System.out.println("NO se pudo ELIMINAR el nuevo elemento en MEDICION");
        }
        return r;
    }
    //4- Modificar un elemento
    public boolean modificar(Medicion m){
        boolean r=false;
        String sql="UPDATE funcionario set temperatura=?,cedulafuncionario=?,fecha=?,hora=?,lugar_marcacion=?"+"WHERE id_medicion=?";
        try{
            con=c.Conectar();
            ps.setFloat(1,m.getTemperatura());
            ps.setString(2,m.getCedulaFuncionario());
            ps.setString(3,m.getFecha());
            ps.setString(4,m.getHora());
            ps.setString(5,m.getLugarMarcacion());
            ps.setString(6,m.getIDMedicion());
            int resultado=ps.executeUpdate();
            if(resultado==0){
                r=true;
            }
        }
        catch(Exception e){
            System.out.println("NO se pudo MODIFICAR el nuevo elemento en FUNCIONARIO");
        }
        return r;
    }
    
    
}
