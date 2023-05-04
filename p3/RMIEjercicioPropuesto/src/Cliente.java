
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Cliente implements Runnable {
    private String host, replica;

    public Cliente(String hostname, String replica) {
        host = hostname;
        this.replica = replica;
    }

    public static void main(String args[]) {
        if (System.getSecurityManager() == null) {
            System.setSecurityManager(new SecurityManager());
        }

        Scanner s = new Scanner(System.in); // Obtener entradas
        ArrayList<Cliente> clientes = new ArrayList<>();
        ArrayList<Thread> hebras = new ArrayList<>();
        int nClientes = 0;

        do {
            System.out.println("Nº de clientes: ");
            nClientes = Integer.parseInt(s.nextLine());

            // Array con todos los clientes (hebras)
            for (int i = 0; i < nClientes; i++) {
                clientes.add(new Cliente("localhost", "replica_0"));// Conecta primera replica por si sólo hay 1
            }

        } while (nClientes < 0);

        // Lanzar hebras
        for (int i = 0; i < clientes.size(); i++) {
            hebras.add(new Thread(clientes.get(i), Integer.toString(i)));
            hebras.get(i).start();
        }
    }

    @Override
    public void run() {
        try {
            Registry registry = LocateRegistry.getRegistry(host, 1099);//Vincular registro
            int donacion = 0;

            // Registro
            System.out.println("Se va a registrar el cliente " + Thread.currentThread().getName() + " en "
                    + this.replica);
            iDonaciones local = (iDonaciones) registry.lookup(this.replica + "donacion");//Utilizar bindeo del objeto 
            int idAtentido = local.registrar(Thread.currentThread().getName()); //Obtener id de la replica atentido el registro
            this.replica = "replica_" + idAtentido;//Actualizar con id de la replica atentido
            System.out.println("Cliente" + Thread.currentThread().getName() + " ha sido registrado en " + this.replica);

            // Donacion
            donacion = new Random().nextInt(100); //Cambiar a cualquier numero TODO
            System.out.println("Cliente" + Thread.currentThread().getName() + " va a donar " + donacion + " a "
                    + this.replica);
            local.donar(Thread.currentThread().getName(), donacion, idAtentido); //Pasa id de la replica que le ha atendido para que le vuelva atender
            System.out.println("Cliente " + Thread.currentThread().getName()+ " ha donado satisfactoriamente");

            // Mostrar total de donaciones
            float total = local.totalDonado(Thread.currentThread().getName());
            System.out.println("(Cliente" + Thread.currentThread().getName() + ") Total donaciones: "
                    + total);
        } catch (Exception e) {
            System.err.println("Error en el Cliente" + Thread.currentThread().getName());
            e.printStackTrace();
        }
    }
}