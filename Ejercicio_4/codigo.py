intentos=0
while (intentos<3):
    usuario = input("usuario: ")
    contraseña = input("contraseña: ")
    if usuario =="":
        print("usuario vacio")
        intentos += 1
    elif usuario==chr(32):
        print("espacios no permitidos")    
        intentos += 1
    elif len(contraseña) < 8:
        print("la contraseña es minima a 8 carecteres")
        intentos += 1
    elif contraseña.isdigit():
        print("la contraseña no puede ser solo numeros")
        intentos += 1
    elif contraseña.isalpha():
        print("la contraseña no puede ser solo letras")
        intentos += 1
    elif usuario =="admin" and contraseña == "Admin2026":
        print("acceso permitido")
        acceso=1
    else:
        intentos +=1
    print("acceso denegado, intentos restantes:", 3-intentos )
    
    while acceso== 1: 
        print("1. clasificar número")
        print("2. categoria de edad y permisos")
        print("3. calcular tarifa final")
        print("4.cerrar sesion")
        print("5. salir") 
        opcion = input ("selecciona una opcion")
