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

client = Calculadora.Client(protocol)

transport.open()

print("hacemos ping al server")
client.ping()

resultado = client.suma(1, 1)
print("1 + 1 = " + str(resultado))
resultado = client.resta(1, 1)
print("1 - 1 = " + str(resultado))
resultado = client.multiplica(2, 2)
print(" 2 x 2 = " + str(resultado))
resultado = client.divida(4, 3)
print(" 4 / 3 = " + str(resultado))
resultado = client.producto_escalar([1,2,3],[2,2,2])
print("producto escalar: "+str(resultado))
resultado = client.producto_vectorial([1,2,3],[2,2,2])
print("producto vectorial: " + str(resultado))


transport.close()
