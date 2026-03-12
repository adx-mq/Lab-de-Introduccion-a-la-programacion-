# Validar que N sea entero
while True:
    try:
        n = int(input("Ingrese el valor de N: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero.")

# Validar el número que se quiere omitir
while True:
    try:
        omitir = int(input("Ingrese el número que desea omitir: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero.")

while n > 0:

    if n == omitir:
        n = n - 1
        continue   # omite ese número

    print(n)
    n = n - 1

print("Salir del ciclo while")