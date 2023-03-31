import glob
import sys
sys.path.append("/home/rubnrosales/Universidad/3Año/DSD/DSD-practicas/practica-2-2-codigo/gen-py")

from calculadora import Calculadora
from calculadora import Calculadora_avanzada

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraHandler:
    def __init__(self):
        self.log = {}
        # Tengo que usar la dirección IP directa (IPv4) debido a que cómo
        # el otro cliente está utilizando la dirección de localhost (IPv6) y
        # solo se puede traducir una vez, en caso contrario daría errores de 
        # conexiones rechazadas porque el puerto queda temporalmente bloqueado
        # ya que considera actividad sospechosa
        self.transporte = TSocket.TSocket("127.0.0.1",9091)
        self.transporte = TTransport.TBufferedTransport(self.transporte)
        self.protocolo = TBinaryProtocol.TBinaryProtocol(self.transporte)
        self.server_client = Calculadora_avanzada.Client(self.protocolo)

    def ping(self):
        print("me han hecho ping()")

    def suma(self, n1, n2):
        print("sumando " + str(n1) + " con " + str(n2))
        return n1 + n2

    def resta(self, n1, n2):
        print("restando " + str(n1) + " con " + str(n2))
        return n1 - n2
    
    def multiplica(self, n1, n2):
        print("multplicando " + str(n1) + " con " + str(n2))
        return n1 * n2
    
    def divida(self, n1, n2):
        print("dividiendo " + str(n1) + " con " + str(n2))
        return n1 / n2 #Divisón entera
    
    def suma_vectorial(self,v1,v2):
        self.transporte.open()
        print("Conectando con un servidor más avanzado...")
        resultado = self.server_client.suma_vectorial(v1,v2)
        print("Obtenida respuesta!")
        self.transporte.close()
        return resultado
    
    def resta_vectorial(self,v1,v2):
        self.transporte.open()
        print("Conectando con un servidor más avanzado...")
        resultado = self.server_client.resta_vectorial(v1,v2)
        print("Obtenida respuesta!")
        self.transporte.close()
        return resultado

    def producto_escalar(self,v1, v2):
        self.transporte.open()
        print("Conectando con un servidor más avanzado...")
        resultado = self.server_client.producto_escalar(v1,v2)
        print("Obtenida respuesta!")
        self.transporte.close()
        return resultado

    def producto_vectorial(self,v1, v2):
        self.transporte.open()
        print("Conectando con un servidor más avanzado...")
        resultado = self.server_client.producto_vectorial(v1,v2)
        print("Obtenida respuesta!")
        self.transporte.close()
        return resultado

    def suma_matriz(self,m1,m2):
        self.transporte.open()
        print("Conectando con un servidor más avanzado...")
        resultado = self.server_client.suma_matriz(m1,m2)
        print("Obtenida respuesta!")
        self.transporte.close()
        return resultado

if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    server.serve()
    print("fin")
