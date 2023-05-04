

import java.rmi.NotBoundException;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface iDonaciones extends Remote {
    int registrar(String cliente) throws RemoteException, NotBoundException;//Registra un cliente

    void donar(String cliente, float cantidad, int id) throws RemoteException, NotBoundException;//Donacion de un cliente

    float totalDonado(String cliente) throws RemoteException, NotBoundException;//Obtiene total donado de los servidores
}
