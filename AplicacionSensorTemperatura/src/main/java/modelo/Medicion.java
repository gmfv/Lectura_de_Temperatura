/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package modelo;

/**
 *
 * @author Diego
 */
public class Medicion {
    private String id_medicion;
    private float temperatura;
    private String cedulafuncionario;
    private String fecha;
    private String hora;
    private String lugar_marcacion;
    
    public Medicion(){ //constructor
        
    }
    // id medicion
    public String getIDMedicion(){
        return id_medicion;
    }
    public void setIDMedicion(String c){
        id_medicion=c;
    }
    // temperatura
    public float getTemperatura(){
        return temperatura;
    }
    public void setTemperatura(float t){
        temperatura=t;
    }
    //cedulafuncionario
    public String getCedulaFuncionario(){
        return cedulafuncionario;
    }
    public void setCedulaFuncionario(String c){
        cedulafuncionario=c;
    }
    //fecha
    public String getFecha(){
        return fecha;
    }
    public void setFecha(String f){
        fecha=f;
    }
    //hora
    public String getHora(){
        return hora;
    }
    public void setHora(String h){
        hora=h;
    }
    //lugar_marcacion
    public String getLugarMarcacion(){
        return lugar_marcacion;
    }
    public void setLugarMarcacion(String l){
        lugar_marcacion=l;
    }
    
}
