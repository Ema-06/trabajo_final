def buscarPrimeraPosicion(palabra: str, letra: str) -> int | None:

    for i in range(len(palabra)):
        if letra == palabra[i]:
            return i


letra = input("Ingrese una letra: ")
palabra = input("Ingrese una palabra: ")
posicion = buscarPrimeraPosicion(palabra, letra)

if posicion is not None:
    print("la letra " + letra + " esta en la posicion: " + str(posicion))
else:
    print("No se encontro dentro de la palabra, la letra deseada")
