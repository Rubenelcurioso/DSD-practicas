import glob
import sys
sys.path.append("/home/rubnrosales/Universidad/3Año/DSD/DSD-practicas/practica-2-2-codigo/gen-py")

from calculadora import Calculadora_avanzada

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraAvanzadaHandler:
    def __init__(self):
        self.log = {}

    def producto_escalar(self,v1, v2):
        resultado = 0.0
        for i in range(0,len(v1)):
            resultado += v1[i] * v2[i]
        return resultado
    
    def producto_vectorial(self,v1, v2):
        resultado = list()
        resultado.append(v1[1]*v2[2]-v1[2]*v2[1])
        resultado.append(v1[2]*v2[0]-v1[0]*v2[2])
        resultado.append(v1[0]*v2[1]-v1[1]*v2[0])
        return resultado



    


if __name__ == "__main__":
    handler = CalculadoraAvanzadaHandler()
    processor = Calculadora_avanzada.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9091)# Operará en el puerto 9091
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    server.serve()
    print("fin")
