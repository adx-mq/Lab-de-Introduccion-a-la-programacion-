from unicodedata import digit


palabra = input("Ingresa una palabra: ")
for i in range(10):
    print(palabra)

edad = int(input("Ingresa tu edad: "))
for i in range(edad, 0, -1):
    print(i)


inicio=int(input("Inicio: "))
final=int(input("Final: "))
resultado=""
for i in range (inicio, final +1):
	if ( i% 2 !=0):
            resultado += str(i) + ","

print(resultado)