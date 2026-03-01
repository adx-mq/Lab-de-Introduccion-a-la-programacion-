intentos=0
while (intentos<3):
    usuario = input("usuario:")
    password = input("Contraseña:")
    if usuario =="":
        print("Usuario vacío")
        intentos += 1
    elif usuario==chr(32):
       print("espacios no permitidos")
       intentos += 1
    elif len(password)<8:
        print("La contraseña es minima a 8 caracteres")
        intentos += 1
        for c in password:
            if not (c.isdigit() or ('a' <= c <= 'z') or ('A' <= c <= 'Z')):
                print("La contraseña debe contener solo letras y números")
                break
        print("Acceso denegado. Intentos restantes:", 3-intentos)

    elif usuario != "admin" or password != "Admin2026":
        intentos += 1 
        break
    elif usuario == "admin" and password == "Admin2026":
        print("Acceso permitido") 
        acceso = 1
      
    while acceso == 1:
        print("Bienvenido al sistema de acceso. Por favor, selecciona una opcion:")
        print("1. Clasificar numero") 
        print("2. Categoria edad y permisos")
        print("3. Calcular tarifa final")
        print("4. Cerrar sesion")
        print("5. Salir")
        opcion = input("Selecciona una opción: ") 
        if opcion == "1": 
            print("Clasificar número ")
        elif opcion  == "2":
            print("Categoria de edad y permisos")
        elif opcion == "3":
            print("Calcular tarifa final")
        elif opcion == "4":
            acceso=0
            break
        elif opcion == "5":
            print ("salir")
            acceso=2
            if acceso==2:
                break 
