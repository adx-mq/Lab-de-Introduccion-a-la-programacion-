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
    elif usuario == "admin" and password == "Admin2026":
     print("Acceso concedido")
     break 

    elif usuario != "admin" or password != "Admin2026":
        intentos += 1 
    print("Acceso denegado. Intentos restantes:", 3-intentos)
