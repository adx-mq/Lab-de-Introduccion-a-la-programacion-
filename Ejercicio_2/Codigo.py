def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2



def decimal_a_binario(num):
    if num == 0:
        return "0"
    
    binario = ""
    while num > 0:
        residuo = num % 2
        binario = str(residuo) + binario
        num = num // 2
    return binario


def decimal_a_octal(num):
    if num == 0:
        return "0"
    
    octal = ""
    while num > 0:
        residuo = num % 8
        octal = str(residuo) + octal
        num = num // 8
    return octal


def decimal_a_hexadecimal(num):
    if num == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        residuo = num % 16
        hexadecimal = hex_chars[residuo] + hexadecimal
        num = num // 16
    return hexadecimal


def mostrar_conversiones(resultado):
    if resultado.is_integer():  # solo si es entero
        entero = int(resultado)

        print("\nConversiones del resultado:")
        print("Binario:", decimal_a_binario(entero))
        print("Octal:", decimal_a_octal(entero))
        print("Hexadecimal:", decimal_a_hexadecimal(entero))
    else:
        print("\nEl resultado no es entero, no se puede convertir exactamente.")



print("Por favor, elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa una opción (1/2/3/4): ")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultado = None

if opcion == '1':
    resultado = suma(num1, num2)
    print(num1, "+", num2, "=", resultado)

elif opcion == '2':
    resultado = resta(num1, num2)
    print(num1, "-", num2, "=", resultado)

elif opcion == '3':
    resultado = multiplicacion(num1, num2)
    print(num1, "*", num2, "=", resultado)

elif opcion == '4':
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = division(num1, num2)
        print(num1, "/", num2, "=", resultado)

else:
    print("Opción inválida")


if resultado is not None:
    mostrar_conversiones(resultado)
