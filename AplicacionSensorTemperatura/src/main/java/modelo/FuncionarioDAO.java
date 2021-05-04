/*
 * Diego Valenzuela - Ing. Mecatronica. 
 */
package modelo;
import controlador.Conexion;
import java.sql.*; // contiene al objeto connection
import java.util.*; //contiene la libreria LIST 

/**
 *
 * @author Diego
 */
public class FuncionarioDAO {
    private Conexion c = new Conexion();
    private Connection con;
    private PreparedStatement ps; 
    private ResultSet rs; 
    
    public FuncionarioDAO(){
        
    }
    //1- Listar
    public List<Funcionario> listar(){
        ArrayList <Funcionario> lista = new ArrayList();
        String sql="SELECT * FROM funcionario";
        try{
            con = c.Conectar(); // me conecto con la base de datos
            ps= con.prepareStatement(sql); 
            rs= ps.executeQuery(); //lista de registros que voy a ir recuperando
            while(rs.next()){
                Funcionario f= new Funcionario();
                f.setCedula(rs.getString("cedula"));
                f.setMail(rs.getString("mail"));
                f.setNombre(rs.getString("nombre"));
                f.setTelefono(rs.getString("telefono"));
                lista.add(f);
            }
            
        }
        catch(Exception e){
            System.out.println("No se pudo listar los funcionarios");
        }
        return lista;
    }
    //2- Agregar un nuevo elemento
    public boolean insetar(Funcionario f){
        boolean r=false;
        String sql="INSERT INTO funcionario (cedula,nombre,telefono,mail)"+"VALUES(?,?,?,?)";
        try{
            con=c.Conectar();
            ps=con.prepareStatement(sql);
            ps.setString(1,f.getCedula());
            ps.setString(2,f.getNombre());
            ps.setString(3,f.getTelefono());
            ps.setString(4,f.getMail());
            int resultado=ps.executeUpdate();
            if(resultado==0){
                r=true;
            }
        }
        catch(Exception e){
            System.out.println("NO se pudo AGREGAR el nuevo elemento en FUNCIONARIO");
        }
        return r;
    }
    //3- Eliminar un elemento
    public boolean eliminar(String CI){ //c es numero de cedula
        boolean r=false;
        String sql="DELETE FROM funcionario WHERE cedula="+CI;
        try{
            con= c.Conectar();
            ps=con.prepareStatement(sql);
            int resultado=ps.executeUpdate();
            if(resultado==0){
                r=true;
            }
        }
        catch(Exception e){
            System.out.println("NO se pudo ELIMINAR el nuevo elemento en FUNCIONARIO");
        }
        return r;
    }
    //4- Modificar un elemento
    public boolean modificar(Funcionario f){
        boolean r=false;
        String sql="UPDATE funcionario set nombre=?,telefono=?,mail=?"+"WHERE cedula=?";
        try{
            con=c.Conectar();
            ps=con.prepareStatement(sql);
            ps.setString(1, f.getNombre());
            ps.setString(2,f.getTelefono());
            ps.setString(3,f.getMail());
            ps.setString(4, f.getCedula());
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
