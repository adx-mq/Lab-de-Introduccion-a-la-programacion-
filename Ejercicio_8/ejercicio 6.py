# ================= FUNCIONES =================

def tablas_for(tablaInicial, tablaFinal, limiteInferior, limiteSuperior):
    for i in range(tablaInicial, tablaFinal + 1):
        print("TABLA DEL ", i)
        for j in range(limiteInferior, limiteSuperior + 1):
            print(i, "X", j, "=", i * j)


def tablas_while(tablaInicial, tablaFinal, limiteInferior, limiteSuperior):
    limiteInferiorTmp = limiteInferior

    while(tablaInicial <= tablaFinal):
        print("TABLA DEL ", tablaInicial)

        while(limiteInferior <= limiteSuperior):
            print(tablaInicial, "X", limiteInferior, "=", tablaInicial * limiteInferior)
            limiteInferior = limiteInferior + 1

        limiteInferior = limiteInferiorTmp
        tablaInicial = tablaInicial + 1


def tablas_do_while(tablaInicial, tablaFinal, limiteInferior, limiteSuperior):
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


# ================= MENÚ =================

def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. FOR")
        print("2. WHILE")
        print("3. DO WHILE")
        print("4. SALIR")

        opcion = input("Selecciona una opción: ")

        if opcion == "4":
            print("Saliendo...")
            break

        # pedir datos (mismos nombres)
        tablaInicial = int(input("INGRESA LA TABLA INICIAL: "))
        tablaFinal = int(input("INGRESA LA TABLA FINAL: "))
        limiteInferior = int(input("INGRESA EL LIMITE INFERIOR: "))
        limiteSuperior = int(input("INGRESA EL LIMITE SUPERIOR: "))

        match opcion:
            case "1":
                tablas_for(tablaInicial, tablaFinal, limiteInferior, limiteSuperior)
            case "2":
                tablas_while(tablaInicial, tablaFinal, limiteInferior, limiteSuperior)
            case "3":
                tablas_do_while(tablaInicial, tablaFinal, limiteInferior, limiteSuperior)
            case _:
                print("Opción inválida")


# ================= EJECUCIÓN =================
menu()