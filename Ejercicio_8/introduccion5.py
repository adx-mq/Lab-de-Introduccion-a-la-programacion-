# ciclos anidados for
#declaramos las variables y las pedimos al usuario
tablaInicial = int(input("INGRESA LA TABLA INICIAL: "))
tablaFinal = int(input("INGRESA LA TABLA FINAL: "))
limiteInferior = int(input("INGRESA EL LIMITE INFERIOR: "))
limiteSuperior = int(input("INGRESA EL LIMITE SUPERIOR: "))

#codigo para que se haga lo que queremos hacer
for i in range(tablaInicial, tablaFinal + 1):
#pedimos que se imprima la tabla del numero i
    print("TABLA DEL ", i)
#imprimimos la tabla del numero i
    for j in range(limiteInferior, limiteSuperior + 1):
#pedimos el limite inferior y el limite superior para que se imprima la tabla del numero i
        print(i, "X", j, "=", i * j)
#pedimos que se imprima la tabla del numero i multiplicada por el numero j, que va desde el limite inferior hasta el limite superior


