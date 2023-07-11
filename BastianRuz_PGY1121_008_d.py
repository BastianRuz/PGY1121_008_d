import funciones as fn
import numpy 
productora = numpy.zeros({10,10},int)

print(fn.mostrar_menu)
opc = fn.validar_menu()
if opc ==1:
    comprarentrada = fn.compra_entrada()
    ubicacion = fn.mostrar_ubi()
    rut=fn.validar_rut()
    nombre = fn.validar_nombre()
    apellido = fn.validar_apellido()
    print("Se ha realizado la compra con exito!")
elif opc == 2:
    cancha=fn.mostrar_ubi()
elif opc == 3:
    asistentes=fn.lista_asistentes()
elif opc == 4:
    total=fn.ganancias_totales()
else:
    print(fn.salir)
        
