# FUNCION CON FOR
def tablas_for(tablaInicial, tablaFinal, limiteInferior, limiteSuperior):
    for i in range(tablaInicial, tablaFinal + 1):
        print("TABLA DEL", i)
        for j in range(limiteInferior, limiteSuperior + 1):
            print(i, "X", j, "=", i * j)


# FUNCION CON WHILE
def tablas_while(tablaInicial, tablaFinal, limiteInferior, limiteSuperior):
    limiteInferiorTmp = limiteInferior

    while tablaInicial <= tablaFinal:
        print("TABLA DEL", tablaInicial)

        while limiteInferior <= limiteSuperior:
            print(tablaInicial, "X", limiteInferior, "=", tablaInicial * limiteInferior)
            limiteInferior += 1

        limiteInferior = limiteInferiorTmp
        tablaInicial += 1


# FUNCION CON DO WHILE (SIMULADO)
def tablas_dowhile(tablaInicial, tablaFinal, limiteInferior, limiteSuperior):
    i = tablaInicial

    while True:
        print("TABLA DEL", i)

        j = limiteInferior
        while True:
            print(i, "X", j, "=", i * j)
            j += 1
            if j > limiteSuperior:
                break

        i += 1
        if i > tablaFinal:
            break


# PROGRAMA PRINCIPAL
def main():

    # VALIDAR TABLAS (3 INTENTOS)
    intentos = 3
    while intentos > 0:
        try:
            tablaInicial = int(input("INGRESA LA TABLA INICIAL: "))
            tablaFinal = int(input("INGRESA LA TABLA FINAL: "))

            if tablaInicial > 0 and tablaFinal > 0 and tablaInicial < tablaFinal:
                break
            else:
                print("ERROR: Valores positivos y tablaInicial < tablaFinal")
        except ValueError:
            print("ERROR: Debes ingresar números válidos")

        intentos -= 1
        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("Demasiados intentos. Fin del programa.")
        return

    # VALIDAR LIMITES (3 INTENTOS)
    intentos = 3
    while intentos > 0:
        try:
            limiteInferior = int(input("INGRESA EL LIMITE INFERIOR: "))
            limiteSuperior = int(input("INGRESA EL LIMITE SUPERIOR: "))

            if limiteInferior > 0 and limiteSuperior > 0 and limiteInferior < limiteSuperior:
                break
            else:
                print("ERROR: Límites positivos y limiteInferior < limiteSuperior")
        except ValueError:
            print("ERROR: Debes ingresar números válidos")

        intentos -= 1
        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("Demasiados intentos. Fin del programa.")
        return

    # MENU
    print("\nMENU DE SELECCION")
    print("1. FOR")
    print("2. WHILE")
    print("3. DO WHILE")

    # VALIDAR OPCION (3 INTENTOS)
    intentos = 3
    while intentos > 0:
        try:
            opcion = int(input("ELIGE UNA OPCION: "))
            break
        except ValueError:
            print("ERROR: Debes ingresar un número válido")

        intentos -= 1
        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("Demasiados intentos. Fin del programa.")
        return

    # MATCH CASE
    match opcion:
        case 1:
            tablas_for(tablaInicial, tablaFinal, limiteInferior, limiteSuperior)
        case 2:
            tablas_while(tablaInicial, tablaFinal, limiteInferior, limiteSuperior)
        case 3:
            tablas_dowhile(tablaInicial, tablaFinal, limiteInferior, limiteSuperior)
        case _:
            print("OPCION NO VALIDA")


# EJECUCION
main()

