# ciclos anidados do while
#  declaramos las variables y las pedimos al usuario

tablaInicial = int(input("INGRESA LA TABLA INICIAL: "))
tablaFinal = int(input("INGRESA LA TABLA FINAL: "))
limiteInferior = int(input("INGRESA EL LIMITE INFERIOR: "))
limiteSuperior = int(input("INGRESA EL LIMITE SUPERIOR: "))

# guardamos el valor original
limiteInferiorTmp = limiteInferior

# simulación do while
while True:
    print("TABLA DEL ", tablaInicial)

    while True:
        print(tablaInicial, "X", limiteInferior, "=", tablaInicial * limiteInferior)
        limiteInferior = limiteInferior + 1

        if not (limiteInferior <= limiteSuperior):
            break

    limiteInferior = limiteInferiorTmp
    tablaInicial = tablaInicial + 1

    if not (tablaInicial <= tablaFinal):
        break