# 🌸 Sistema de Control de Acceso en Python 🌸

## Descripción del programa 💻🔐
Desarrollar un código que permita solicitar un **usuario** y una **contraseña**, aplicando validaciones obligatorias y un límite máximo de intentos.

El programa valida que:
- El usuario no esté vacío.
- No contenga espacios.
- La contraseña tenga mínimo 8 caracteres.
- Solo contenga letras y números.
- Solo permita 3 intentos.

Este sistema demuestra el uso correcto de estructuras de control y validaciones en Python de forma clara y organizada.

---
---

# 🧠 Explicación del Funcionamiento

```python
intentos = 0
```

Aquí se crea la variable `intentos` para contar los intentos fallidos.  
El sistema solo permite un máximo de **3 intentos**, garantizando control y seguridad.

```python
while (intentos < 3):
```

El ciclo `while` permite repetir el proceso mientras los intentos sean menores a 3.  
Cuando el contador llega a 3, el programa termina automáticamente.

```python
usuario = input("usuario: ")
password = input("Contraseña: ")
```

Se solicitan los datos al usuario y se almacenan en variables para poder validarlos después.

```python
if usuario == "":
```

Se verifica que el usuario no esté vacío.  
Si lo está, el sistema muestra un mensaje y descuenta un intento.


```python
elif usuario == chr(32):
```

`chr(32)` representa un espacio en blanco.  
Si el usuario ingresa solo un espacio, se considera inválido y se descuenta un intento.

```python
elif len(password) < 8:
```

La función `len()` cuenta los caracteres de la contraseña.  
Si tiene menos de 8 caracteres, el sistema muestra un mensaje de error.


```python
for c in password:
```

El ciclo `for` revisa cada carácter de la contraseña de manera individual.

```python
if not (c.isdigit() or ('a' <= c <= 'z') or ('A' <= c <= 'Z')):
```

Se verifica que cada carácter sea:

- Número  
- Letra minúscula  
- Letra mayúscula  

Si encuentra un carácter inválido (como símbolos), se muestra un mensaje de error.

```python
elif usuario == "admin" and password == "Admin2026":
```

Si el usuario y la contraseña coinciden exactamente,  
se concede el acceso y el ciclo se detiene con `break`.

```python
elif usuario != "admin" or password != "Admin2026":
```

Si los datos no coinciden, se descuenta un intento.

```python
print("Acceso denegado. Intentos restantes:", 3 - intentos)
```

Se muestra cuántos intentos restantes quedan disponibles.

- Variables  
- Ciclo `while`  
- Ciclo `for`  
- Condicionales `if` y `elif`  
- Operadores lógicos (`and`, `or`, `not`)  
- Funciones `input()`, `print()`, `len()`, `isdigit()`, `chr()`  
- Control de flujo con `break`  

---
---
# 🪷🪷

Este sistema implementa un control de acceso básico con validaciones obligatorias y límite de intentos.  
El flujo es lógico, ordenado y asegura que se cumplan las condiciones antes de permitir el acceso.

El programa cumple con los requerimientos funcionales establecidos y demuestra la aplicación correcta de conceptos fundamentales de programación en Python ✨.
