def buscarPrimeraPosicion(palabra: str, letra: str) -> int | None:

    for i in range(len(pb)):
        if lt == pb[i]:
            return i


lt = input("Ingrese una letra: ")
pb = input("Ingrese una palabra: ")
ubicacion = buscarPrimeraPosicion(palabra, letra)

if posicion is not None:
    print("la letra " + letra + " esta en la posicion: " + str(posicion))
else:
    print("No se encontro dentro de la palabra, la letra deseada")
