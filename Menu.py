from agregarCancion import agregarNuevaCancion
from buscarCancion import buscarCancion
from modificarCancion import modificarCancion


cancion1 = {"Titulo": "Me va a extrañar", "Artista": "Ricardo Montaner", "Letra": "Cada mañana el sol nos dio en la cara "}
cancion2 = {"Titulo": "Amigos", "Artista": "Alejandro Lerner", "Letra": "Que un amigo es una luz brillando en la oscuridad "}
cancion3 = {"Titulo": "Universo paralelo", "Artista": "La K'onga", "Letra": "Eres el centro del cosmos mi universo paralelo"}
cancion4 = {"Titulo": "Desde que no estas aqui", "Artista": "Los nocheros", "Letra": "Como quisiera saber si es que aun me recuerdas "}
cancion5 = {"Titulo": "Dos mundos", "Artista": " Luciano Pereyra", "Letra": "Hay un mundo entre tú y yo que nos aleja Una forma de vivir la vida que nos separa "}
listaCanciones = [cancion1, cancion2, cancion3, cancion4, cancion5] 


def textoMenu():
    print ("Si quiere agregar una canción, Opcion1")
    print("Si quiere buscar una canción, Opcion 2")
    print("Si quiere modificar una canción, Opcion3")
    print("Si quiere salir, Opcion4")
    elecUser= int(input())
    if elecUser == 1:
        agregarNuevaCancion(listaCanciones)
    elif elecUser == 2: 
        buscarCancion(listaCanciones)
    elif elecUser == 3:
        modificarCancion(listaCanciones) 
    else:
        print("salir") 

textoMenu()