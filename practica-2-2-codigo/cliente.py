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

def menu_basico():
    print("Seleccione una opción:")
    print("0 - Salir")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")
    print("5 - Operaciones vectoriales")
    print("6 - Operaciones matriciales")

    opcion = int(input("Opción: "))

    return opcion

def pedir_vector():
    n = int(input("Ingrese la dimensión del vector: "))
    vector = []
    for i in range(n):
        valor = float(input(f"Ingrese el valor {i+1} del vector: "))
        vector.append(valor)
    return vector

def pedir_matriz():
    n = int(input("Ingrese la cantidad de filas de la matriz: "))
    m = int(input("Ingrese la cantidad de columnas de la matriz: "))
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            valor = float(input(f"Ingrese el valor ({i+1}, {j+1}) de la matriz: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def inputOperandos(opcion):
    if opcion>=1 and opcion<5:
        operando1 = int(input("Ingrese el primer número: "))
        operando2 = int(input("Ingrese el segundo número: "))
        return opcion,operando1,operando2

    elif opcion == 5:
        print("Seleccione el tipo de operación avanzada:")
        print("1 - Suma vectores")
        print("2 - Resta vectores")
        print("3 - Producto escalar")
        print("4 - Producto vectorial")

        opcion_avanzada = int(input("Operacion a elegir: "))
        v1 = pedir_vector()
        v2 = pedir_vector()

        return opcion,opcion_avanzada,v1,v2


    elif opcion == 6:
        print("Seleccione el tipo de operación avanzada:")
        print("1 - Suma matrices")
        print("2 - Resta matrices")
        print("3 - Multiplicacion matrices")
        print("4 - Division matrices")

        opcion_avanzada = int(input("Operacion a elegir: "))
        m1 = pedir_matriz()
        m2 = pedir_matriz()
        return opcion,opcion_avanzada,m1,m2
    
    else:
        print("Opción inválida")

def realizaOperacion(tupla,cliente):
    if len(tupla)==3: #Operacion calculadora basica
        if tupla[0]==1:
            print(cliente.suma(tupla[1],tupla[2]))
        elif tupla[0]==2:
            print(cliente.resta(tupla[1],tupla[2]))
        elif tupla[0]==3:
            print(cliente.multiplica(tupla[1],tupla[2]))
        elif tupla[0]==4:
            print(cliente.divida(tupla[1],tupla[2]))
    elif len(tupla)==4:
        if tupla[0]==5: #Operacion vector
            if tupla[1]==1:
                print(cliente.suma_vectorial(tupla[2],tupla[3]))
            elif tupla[1]==2:
                print(cliente.resta_vectorial(tupla[2],tupla[3]))
            elif tupla[1]==3:
                print(cliente.producto_escalar(tupla[2],tupla[3]))
            elif tupla[1]==4:
                print(cliente.producto_vectorial(tupla[2],tupla[3]))
        elif tupla[0]==6:
            if tupla[1]==1:
                print(cliente.suma_matriz(tupla[2],tupla[3]))
            elif tupla[1]==2:
                print(cliente.resta_matriz(tupla[2],tupla[3]))
            elif tupla[1]==3:
                print(cliente.multiplica_matriz(tupla[2],tupla[3]))
            elif tupla[1]==4:
                print(cliente.divide_matriz(tupla[2],tupla[3]))

            

client = Calculadora.Client(protocol)

transport.open()

opcion = menu_basico()
tupla = inputOperandos(opcion)
realizaOperacion(tupla,client)


transport.close()
