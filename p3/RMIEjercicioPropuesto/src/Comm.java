
import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import javax.sql.rowset.spi.SyncResolver;
import javax.swing.plaf.synth.Region;

public class Comm extends UnicastRemoteObject implements iComms {
    private iComms replica_comm;
    private Registry registro; // Registro de objeto remoto
    private Map<String, Float> registrados;
    String host;
    private int idReplica, subTotal;
    public static int nReplicas = 0;

    protected Comm(String hostname, int id) throws RemoteException {
        super();
        // TODO Auto-generated constructor stub
        registrados = new HashMap<String, Float>();
        registro = LocateRegistry.getRegistry(hostname, 1099);
        host = hostname;
        idReplica = id;
        subTotal = 0;
        nReplicas++;
    }

    @Override
    public synchronized int registrarCliente(String nombre) throws RemoteException, NotBoundException {
        boolean existe = false;
        int idReplicaMenor = 0; // id de la replica con menor registrados
        int nRegistros = getNumRegistrados(); // Nº de registrados
        // TODO Auto-generated method stub
        for (int i = 0; i < nReplicas && !existe; i++) {// Iterar sobre todas las replicas;
            replica_comm = (iComms) registro.lookup("replica_" + i); // Buscar en el registro el objeto remoto
                                                                     // replica i
            if (replica_comm.existeCliente(nombre))// Comprueba en replicas no este registrado
                existe = true;
            if (replica_comm.getNumRegistrados() < nRegistros) {// Replica i menor registrados, asignamos
                idReplicaMenor = i;
                nRegistros = replica_comm.getNumRegistrados();
            }
        }

        if (existe)// Si se sale del bucle porque existe es más eficiente poner en este orden la
                   // condicion
            throw new RemoteException("Ya existe " + nombre + " en una replica\n");
        else {
            replica_comm = (iComms) registro.lookup("replica_" + idReplicaMenor); // Buscamos en el registro el objeto
                                                                                  // remoto de replica con menor
                                                                                  // registrados
            replica_comm.registrar(nombre);
            System.out.println("Cliente: " + nombre + " registrado en replica " + idReplicaMenor + "\n");
        }
        return idReplicaMenor; // Retornar replica donde se produce registro
    }

    @Override
    public synchronized void donar(String cliente, float cantidad, int id) throws RemoteException, NotBoundException {// Revisar
                                                                                                                      // sea
                                                                                                                      // donado
                                                                                                                      // donde
        // se registra
        replica_comm = (iComms) registro.lookup("replica_" + id);
        if (replica_comm.existeCliente(cliente)) {
            // Comprobar cliente exista
            // Actualiza
            // con la
            // suma
            // del
            // valor
            // anterior
            replica_comm.actualizaCliente(cliente, cantidad);
            replica_comm.actualizaSubTotal(cantidad);
            System.out.println("Actualizada donacion de " + cliente + " con una cantidad de " + cantidad + "\n");
        } else
            throw new RemoteException("El cliente " + cliente + " no existe\n");
    }

    public int getNumRegistrados() throws RemoteException {
        return registrados.size();
    }

    @Override
    public synchronized float getTotalDonado(String cliente) throws RemoteException, NotBoundException {
        // TODO Auto-generated method stub
        boolean existe = false;
        float total = 0f;
        for (int i = 0; i < nReplicas; i++) {// Iterar sobre todas las replicas
            replica_comm = (iComms) registro.lookup("replica_" + i);
            if(replica_comm.existeCliente(cliente)){//Si existe el cliente
                if(replica_comm.getRegistrados().get(cliente) > 0)//Si tiene alguna donacion
                    existe = true;
            }
            total += replica_comm.getsubTotal();//Suma los subtotales
        }

        if(!existe)//Si no existe no devolver la suma
            throw new RemoteException("El cliente "+cliente+" no existe\n");

        return total;
    }

    public float getsubTotal() throws RemoteException {
        return subTotal;
    }

    @Override
    public boolean existeCliente(String cliente) throws RemoteException {
        // TODO Auto-generated method stub
        return registrados.containsKey(cliente);
    }

    public void registrar(String nombre) throws RemoteException {// El registro debe ser síncrono debido a
        // que puede darse el caso que se
        // registren 2 iguales al mismo tiempo
        registrados.put(nombre, 0f);
    }

    public Map<String, Float> getRegistrados() throws RemoteException {
        return registrados;
    }

    public void actualizaSubTotal(float cantidad) throws RemoteException {
        subTotal += cantidad;
    }

    public void actualizaCliente(String nombre, float cantidad) throws RemoteException{
        registrados.put(nombre,cantidad);
    }
}
