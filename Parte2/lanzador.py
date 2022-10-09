from Parte2.swag import swag
def lanzar():
    eleccion = 1
    while eleccion != "2":
        eleccion = input("¿Qué quieres hacer?\n(1) Ejecutar el Algoritmo Swag\n(2) Salir\nElección: ")
        if eleccion == "1":
            num = int(input("¿Cuántas veces quieres entrenar la red neuronal?\n")) # epoch
            tamaño = int(input("¿Cuántas veces quieres ejecutar el entreno de la red neuronal?\n")) #bach size
            raiz = int(input("¿Cual es la raíz de la red neuronal?\n")) #seed
            swag(num, tamaño, raiz)