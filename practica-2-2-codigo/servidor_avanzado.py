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

    def suma_vectorial(self,v1,v2):
        if len(v1) != len(v2):
            raise ValueError("Los vectores deben tener misma dimension")
        print("Calculando suma")
        resultado = list()
        for i in range(0,len(v1)):
            resultado.append(v1[i]+v2[i])
        return resultado
    
    def resta_vectorial(self,v1,v2):
        if len(v1) != len(v2):
            raise ValueError("Los vectores deben tener misma dimension")
        print("Calculando resta")
        resultado = list()
        for i in range(0,len(v1)):
            resultado.append(v1[i]-v2[i])
        return resultado

    def producto_escalar(self,v1, v2):
        if len(v1) != len(v2):
            raise ValueError("Los vectores deben tener misma dimension")
        print("Calculando producto escalar")
        resultado = 0.0
        for i in range(0,len(v1)):
            resultado += v1[i] * v2[i]
        return resultado
    
    def producto_vectorial(self,v1, v2):
        if len(v1) != 3 or len(v2) != 3:
            raise ValueError("Los vectores deben ser 3 dimensiones")
        print("Calculando producto vectorial")
        resultado = list()
        resultado.append(v1[1]*v2[2]-v1[2]*v2[1])
        resultado.append(v1[2]*v2[0]-v1[0]*v2[2])
        resultado.append(v1[0]*v2[1]-v1[1]*v2[0])
        return resultado
    
    def suma_matriz(self,m1, m2):
        print("Calculando suma de matrices")
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        resultado = [[0 for j in range(len(m1[i]))] for i in range(len(m1))] # inicializar resultado como una matriz de ceros
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                resultado[i][j] = m1[i][j] + m2[i][j] 
        return resultado
    
    def resta_matriz(self,m1, m2):  
        print("Calculando resta de matrices")
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        
        resultado = [[0 for j in range(len(m1[i]))] for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                resultado[i][j] = m1[i][j] - m2[i][j] 
        return resultado
    
    def multiplica_matriz(self,m1, m2):
        print("Calculando multiplicacion de matrices")
        if len(m1[0]) != len(m2): #Columnas de m1 == Filas de m2
            raise ValueError("El número de columnas de la matriz 1 debe ser igual al número de filas de la matriz 2")
        
        resultado = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
        
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    resultado[i][j] += m1[i][k] * m2[k][j]
        return resultado
    
    def divide_matriz(self,m1, m2):
        print("Calculando division de matrices")
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        
        resultado = [[0 for j in range(len(m1[i]))] for i in range(len(m1))]
        
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                if m2[i][j] == 0:
                    raise ValueError("No se puede dividir entre cero")
                resultado[i][j] = m1[i][j] / m2[i][j]  # dividir los elementos correspondientes y asignarlos a la posición correspondiente en la matriz "resultado"
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
