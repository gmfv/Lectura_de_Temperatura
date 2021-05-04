/*
 * Diego Valenzuela - Ing. Mecatronica.
 */
package modelo;

/**
 *
 * @author Diego
 */
public class Funcionario {
    private String cedula;
    private String nombre;
    private String telefono;
    private String mail;
    
    public Funcionario(){ // constructor
        
    }
    //cedula
    public String getCedula(){
        return cedula;
    }
    public void setCedula(String r){
        cedula=r;
    }
    //nombre
    public String getNombre(){
        return nombre;
    }
    public void setNombre(String r){
        nombre=r;
    }
    //telefono
    public String getTelefono(){
        return telefono;
    }
    public void setTelefono(String r){
        telefono=r;
    }
    //mail
    public String getMail(){
        return mail;
    }
    public void setMail(String r){
        mail=r;
    }
    
}
