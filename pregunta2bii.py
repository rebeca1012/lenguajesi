"""
Alumno: Rebeca Ledesma
Carné: 15-10771
Lenguajes de Programación I
Tarea 3
Pregunta 2.b.ii
"""
# Importa el módulo os para interactuar con el SO y el módulo threading para crear hilos
import os
import threading

# Inicializa una variable global para almacenar el número total de archivos.
total = 0

# Inicializa un bloqueo para evitar condiciones de carrera al actualizar total.
lock = threading.Lock()

"""
Esta función cuenta el número total de archivos en un directorio y sus subdirectorios.

Recibe como parámetro la ruta del directorio a analizar.

"""
def count_files(path):
    
    # Declara total como global para poder modificarla.
    global total

    # Usa os.walk para iterar sobre todos los archivos y directorios en la ruta dada.
    for root, dirs, files in os.walk(path):
        # Para cada archivo en el directorio actual, incrementa total.
        for file in files:
            # Adquiere el bloqueo antes de modificar total para evitar condiciones de carrera.
            lock.acquire()
            total += 1
            # Libera el bloqueo después de modificar total.
            lock.release()

        # Para cada subdirectorio en el directorio actual, crea un nuevo hilo que ejecuta count_files en ese subdirectorio.
        for dir in dirs:
            thread = threading.Thread(target=count_files, args=(os.path.join(root, dir),))
            thread.start()



pth = input("ingrese la ruta del directorio")
count_files(pth)

# Esperar a que todos los hilos terminen
hiloprinc = threading.currentThread()
for thread in threading.enumerate():
    if thread is not hiloprinc:
        thread.join()

# Imprimir el total de archivos
print("Total de archivos: ", total)



