def listarDespachos(despachos):
    print("\nDespachos: \n")
    for des in despachos:
        datos = "Cliente: {0} - Dirección: {1} - Ciudad: {2} - Telefono: {3} - Unidades: {4} - Observación: {5} - Fecha: {6}"
        print(datos.format(des[1], des[2], des[3], des[4], des[5], des[6], des[7]))
    print("")

def pedirDatosRegistro():
    cliente = input("Ingresa el cliente: ")
    direccion = input("Ingresa la dirección: ")
    ciudad = input("Ingresa la ciudad del destinatario: ")
    telefono = input("Ingresa el telefono: ")

    unidadesCorrectas = False
    while(not unidadesCorrectas):
        unidades = input("Ingresa la cantidad de elementos a enviar: ")
        if unidades.isnumeric():
            if(int(unidades) > 0):
                unidadesCorrectas = True
                unidades = int(unidades)
            else:
                print("La cantidad debe ser mayor a 0!")
        else:
            print("La cantidad debe ser un valor numerico!")
    
    observacion = input("Ingresa una observación: ")
    fecha = input("Ingresa la fecha (yyyy-mm-dd) : ")

    despacho = (cliente, direccion, ciudad, telefono, unidades, observacion, fecha)
    return despacho 