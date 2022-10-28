 
def modificarCancion(listaCanciones):
    tituloBuscado = input("Ingrese el titulo que desea buscar:") 
    encontradoEn =-1
    for i in range(len(listaCanciones)):
        if (listaCanciones[i]["Titulo"] == tituloBuscado):
            encontradoEn  = i 

    if encontradoEn != -1:
        nuevoTitulo = input ("Ingrese el nuevo Titulo:")
        listaCanciones[encontradoEn]["Titulo"] = nuevoTitulo
        print ("El titulo nuevo es: ", listaCanciones)
    else:
        print("No existe el titulo")
