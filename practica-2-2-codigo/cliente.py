import sys
sys.path.append("/home/rubnrosales/Universidad/3Año/DSD/DSD-practicas/practica-2-2-codigo/gen-py")
from calculadora import Calculadora

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket("localhost", 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

# def printMenu():
#     print ("""===Menu===
#                 1. Suma
#                 2. Resta
#                 3. Multiplicacion
#                 4. Division 
#                 5. Vectores""")

# def introParams(opcion):
#     if opcion>0 and opcion<5:
#         param1,param2 = input("Introduzca 2 operandos").split()
#         return param1,param2
#     if opcion == 5:
#         v1,v2 = list()
#         for i in range(3):
#             #param1,param2 = int(input("Introduzca siguiente coordenada de los 2 vectores"))
#             v1.append(param1), v2.append(param2)
#         return v1,v2
#     else:
#         print("Error")

client = Calculadora.Client(protocol)

transport.open()

print("hacemos ping al server")
client.ping()

# printMenu()
# opcion = int(input("Seleccione una opcion"))
# introParams(opcion)

# resultado = client.suma(1, 1)
# print("1 + 1 = " + str(resultado))
# resultado = client.resta(1, 1)
# print("1 - 1 = " + str(resultado))
# resultado = client.multiplica(2, 2)
# print(" 2 x 2 = " + str(resultado))
# resultado = client.divida(4, 3)
# print(" 4 / 3 = " + str(resultado))
v1 = [1.0,2.0,3.0]
v2 = [2.0,2.0,2.0]
resultado = client.producto_escalar(v1,v2)
print("producto escalar: "+str(resultado))
resultado = client.producto_vectorial([1.0,2,3],[2,2,2])
print("producto vectorial: " + str(resultado))


transport.close()
