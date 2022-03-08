from BD.conexion import DAO
import funciones


def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("------Menú Principal------")
            print("1. Listar Despachos")
            print("2. Registrar Despachos")
            print("3. Actualizar Despachos")
            print("4. Eliminar Despachos")
            print("5. Salir")
            print("--------------------------")
            opcion = int(input("\nSeleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese una opción nuevamente.")
            elif opcion == 5:
                print("Gracias por utilizar este sistema.")
                continuar = False
                return
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            despachos = dao.listarDespachos()
            if(len(despachos)) > 0:
                funciones.listarDespachos(despachos)
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")
    elif opcion == 2:
        despacho = funciones.pedirDatosRegistro()
        try:
            dao.registrarDespacho(despacho)
        except:
            print("Ocurrio un error")
    elif opcion == 3:
        print("")
    elif opcion == 4:
        print("")
    else:
        print("Opcion no valida")


menuPrincipal()
        

