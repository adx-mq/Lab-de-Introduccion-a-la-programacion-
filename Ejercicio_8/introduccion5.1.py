# ciclos anidados while 
#declaramos las variables y las pedimos al usuario
tablaInicial = int(input("INGRESA LA TABLA INICIAL: "))
tablaFinal = int(input("INGRESA LA TABLA FINAL: "))
limiteInferior = int(input("INGRESA EL LIMITE INFERIOR: "))
limiteSuperior = int(input("INGRESA EL LIMITE SUPERIOR: "))

#codigo para que se haga lo que queremos hacer
limiteInferiorTmp = limiteInferior
while(tablaInicial <= tablaFinal):
#pedimos que se imprima la tabla
    print("TABLA DEL ", tablaInicial)
    #tablaInicial = tablaInicial + 1

    while(limiteInferior <= limiteSuperior):
        print(tablaInicial, "X", limiteInferior, "=", tablaInicial * limiteInferior)
        limiteInferior = limiteInferior + 1
    limiteInferior = limiteInferiorTmp
    tablaInicial = tablaInicial + 1

