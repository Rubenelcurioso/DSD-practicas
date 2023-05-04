
import java.rmi.NotBoundException;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.Map;

public interface iComms extends Remote {
   public int registrarCliente(String nombre) throws RemoteException, NotBoundException;//Registra cumpliendo las condiciones

   public void donar(String cliente, float cantidad, int id) throws RemoteException, NotBoundException;//Dona cumpliendo las condiciones

   public float getTotalDonado(String cliente) throws RemoteException, NotBoundException;//Obtiene el total cumpliendo condiciones

   public float getsubTotal() throws RemoteException; //Obtiene subtotal

   public boolean existeCliente(String cliente) throws RemoteException;//Comprueba que cliente existe en diccionario

   public int getNumRegistrados() throws RemoteException;//Obtiene el nº de registrados en el diccionario

   public void registrar(String nombre) throws RemoteException;//Registra el nombre en el diccionario

   public void actualizaSubTotal(float cantidad) throws RemoteException;//Actualiza el subtotal con la cantidad

   public void actualizaCliente(String nombre, float cantidad) throws RemoteException;//Actualiza un cliente en el diccionario

   public Map<String, Float> getRegistrados() throws RemoteException;//Obtiene el diccionario (Usado para DEBUG)

}
