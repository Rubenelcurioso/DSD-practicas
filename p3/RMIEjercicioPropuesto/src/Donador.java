

import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;
import java.net.MalformedURLException;

public class Donador extends UnicastRemoteObject implements iDonaciones {
    private Comm replica;

    public Donador(Comm replica) throws RemoteException{
        this.replica = replica;
    }

    @Override
    public synchronized int registrar(String cliente) throws RemoteException, NotBoundException {
        // TODO Auto-generated method stub
        return replica.registrarCliente(cliente);
    }

    @Override
    public void donar(String cliente, float cantidad,int id) throws RemoteException, NotBoundException {
        // TODO Auto-generated method stub
        replica.donar(cliente, cantidad, id);
    }

    @Override
    public float totalDonado(String cliente) throws RemoteException, NotBoundException {
        // TODO Auto-generated method stub
        return replica.getTotalDonado(cliente);
    }
 
}
