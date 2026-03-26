# 🌸 Creación de un entorno virtual en Python (Windows)

Este documento explica **paso a paso** cómo crear y usar un **entorno virtual en Python**. Está pensado para trabajar de forma ordenada y correcta en proyectos de Python.

## ✔️ ¿Qué se necesita?

Antes de comenzar, es necesario contar con lo siguiente:

* Sistema operativo **Windows**
* **Python 3** instalado
* **PowerShell**
* Una carpeta para el proyecto

Para verificar que Python esté instalado correctamente, ejecuta:

```powershell
python --version
```
<img width="573" height="42" alt="image" src="https://github.com/user-attachments/assets/66c00ac7-d568-48ac-b950-bc12dff305d3" />


##  Pasos para crear un entorno virtual

### 📂 Paso 1: Entrar a la carpeta del proyecto

Primero, abre PowerShell y muévete a la carpeta donde trabajarás tu proyecto.

Ejemplo:
```powershell
cd Desktop
cd ProyectoPython
```

Este paso es importante porque el entorno virtual se creará **dentro de esta carpeta**.


### Paso 2: Crear el entorno virtual

Una vez dentro de la carpeta del proyecto, ejecuta el siguiente comando:

```powershell
python -m venv venv
```

Esto creará una carpeta llamada:

```
venv/
```
<img width="360" height="235" alt="image" src="https://github.com/user-attachments/assets/78db9213-0bc9-4cfd-afff-dfa25381574a" />

En esta carpeta se guardan Python y las librerías del proyecto.

---

###  Paso 3: Activar el entorno virtual

Para activar el entorno virtual, escribe:

```powershell
venv\Scripts\activate
```

Si el entorno se activó correctamente, verás algo como:

```
(venv)
```

antes de la ruta en la terminal.

---

###  Paso 4: Instalar librerías

Con el entorno virtual activo, las librerías que se instalen solo afectarán a este proyecto.

Ejemplo de instalación:

```powershell
pip install numpy
```
<img width="641" height="172" alt="image" src="https://github.com/user-attachments/assets/efcf2a48-37a6-4bbf-aa92-9bd1ac5b6cd9" />

---

### 🙈 Paso 5: Usar librerías en Python

Las librerías se utilizan dentro de archivos `.py`, no directamente en PowerShell.

Ejemplo de archivo Python:

```python
import numpy as np
= np.
print(numeros)
```
<img width="486" height="386" alt="image" src="https://github.com/user-attachments/assets/d3336b21-f521-4dc8-9ff9-b4e549ac03da" />

Para ejecutar el archivo:

```powershell
python main.py
```

---

###  Paso 6: Evitar subir el entorno virtual a GitHub

El entorno virtual no debe subirse al repositorio. Para ello, crea un archivo `.gitignore` y agrega:

```gitignore
venv/
```

---

## ✨ Listo ✨

🌷 **Entorno virtual creado correctamente**
