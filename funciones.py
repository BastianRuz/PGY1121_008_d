import numpy
listarut = []
productora = numpy({10,10},int)
fecha: 11/7/2023
platinum = {120.000}
gold = {80.000}
silver = {50.000}
acum_dinero = 0
contador_dinero = 0


def validar_nombre():
    while True:
       nombre = input ("ingrese su nombre")
       if len(nombre.strip) >=3:
         return nombre 
       else:
            print("ERROR! SU NOMBRE DEBE TENER ALMENOS 3 O MÁS CARACTERES!")


def validar_apellido():
    while True:
        apellido = input ("ingrese su apellido")
        if len(apellido.strip) >=3:
            return apellido
        else:
            print("ERROR! SU APELLIDO DEBE TENER ALMENOS 3 o MÁs CARACTERES! ")

def validar_rut():
    while True:
        try:
            rut =int(input("ingrese su rut sin puntos ni número verificado"))
            if len(rut.strip) ==8:
                listarut.append[rut]
                return rut
            else:
                print("ERROR! DEBE INGRESAR SU RUT CON NÚMEROS ENTEROS!")
        except:
            print("DEBE INGRESAR ")

def mostrar_menu():
    print("""Hola!, Bienvenidos a Creativos.cl: ingrese una de las opciones

    1. Comprar entradas
    2. Mostrar ubicaciones disponible
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir
    """)

def validar_menu():
    while True:
        try:
             opc=int(input("ingrese su opción:"))
             if opc in (1,2,3,4,5):
                 return opc
             else:
                 print("ERROR! debe ingresar una de las opciones!")
        except:
            print("ERROR! debe ingresar un número entero")
            
def mostrar_ubi():
    while True:
        for x in range (10):
            print(f"fila {x+1}",end =" ")
        for y in range (10):
            print(productora[x][y],end=" ")
           
        print(" ")
            
def compra_entrada():
    while True:
        try:
            entrada=int(input("ingrese la cantidad a comprar(MAX 3 ENTRADAS)"))
            if entrada >=1 and entrada <=3:
                return entrada
            else:
                print ("ERROR! DEBE INGRESAR UNA CANTIDAD CORRECTA")
        except:
            print("ERROR!DEBE INGRESAR NÚMEROS ENTEROS")


def mostrar_lugar():
      while True:
        for x in range (10):
            print(f"fila {x+1}",end =" ")
        for y in range (10):
            print(productora[x][y],end=" ")
           
        print(" ")

def salir():
    print(f"Gracias por su visita {validar_nombre}, fecha{fecha}")

def lista_asistentes():
    print({listarut})

def ganancias_totales():
    print(f"""

    ENTRADAS              |      CANTIDAD      |      TOTAL      |  
    --------------------------------------------------------------
    Platinum ${platinum}  | {contador_dinero}  |  {acum_dinero}  |
    --------------------------------------------------------------
    Gold     ${gold}      | {contador_dinero}  |  {acum_dinero}  |
     --------------------------------------------------------------
    Silver   ${silver}    | {contador_dinero}  |  {acum_dinero}  | 
    
    """)


def validar_filas():
    while True:
        try:
            fila = int(input("ingrese en que fila donde se posicionará (del 1 al 10): "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                if fila in [1,3]:
                    acumulador_dinero =+ platinum
                elif fila in [4,6]:
                    acumulador_dinero =+ gold
                elif fila in [7,8]:
                    acumulador_dinero =+ silver
                return fila
            else:
                print ("ERROR! INGRESE UNA FILA DEL 1 AL 10")
        except:
            print("ERROR! debe ingresar numeros enteros")

def validar_culumna():
    while True:
        try:
            columna = int (input("Ingrese en que fila se posicionará (del 1 al 10): "))
            if columna in (1,2,3,4,5,6,7,8,9,10):
             return columna
            else:
                print ("ERROR! INGRESE UNA FILA DEL 1 AL 10")
        except:
            print ("ERROR! debe ingresar números enteros")


    



