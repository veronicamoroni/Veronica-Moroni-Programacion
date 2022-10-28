def buscarCancion(listaCanciones):
    cancionabuscar = input("Ingrese el Titulo de la cancion que quiere buscar:")
      
    def imprimirCancion(cancion):
        print ("El nombre es:", cancion ["Titulo"])
        print ("El artista es:", cancion ["Artista"])
        print ("La letra es:", cancion ["Letra"])


    for cancion in listaCanciones:
        if cancion ["Titulo"] == cancionabuscar: 
            imprimirCancion(cancion)
            return
    print ("No encontrado")

   