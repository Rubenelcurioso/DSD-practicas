
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

public class Servidor {
    public static void main(String[] args) {
        if (System.getSecurityManager() == null) {
            System.setSecurityManager(new SecurityManager());
        }

        try {
            Scanner s = new Scanner(System.in); // Obtener entrada
            int nReplicas = 0;
            do {
                System.out.println("Nº de replicas: ");
                nReplicas = Integer.parseInt(s.nextLine());
            } while (nReplicas <= 0);

            Registry registro = LocateRegistry.createRegistry(1099);//Crear registro

            // Instanciar n réplicas
            for (int i = 0; i < nReplicas; i++) {
                String objetoRemoto = "replica_" + i;//Nombre del objeto para bind

                Comm replica = new Comm("localhost", i); // Servidor-servidor
                Naming.rebind(objetoRemoto, replica);

                Donador donaciones = new Donador(replica); // Cliente-servidor
                Naming.rebind(objetoRemoto + "donacion", donaciones);

                System.out.println(objetoRemoto + " lista");
            }

            System.out.println("Todas las replicas han iniciado correctamente");
        } catch (Exception e) {
            System.err.println("Replica server exception:");
            e.printStackTrace();
        }
    }
}
