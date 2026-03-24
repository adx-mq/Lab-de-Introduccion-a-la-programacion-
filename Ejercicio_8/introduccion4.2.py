print("Cual tabla inicial quieres?")
tablaInicial = int(input())
print("Cual tabla final quieres?")
tablaFinal = int(input())
for i in range(tablaInicial, tablaFinal + 1, 1):
    print("tabla = " + str(i))
    for j in range(1, 10 + 1, 1):
        print(str(i) + " X " + str(j) + "  =  " + str(i + j))
