"""
Alumno: Rebeca Ledesma
Carné: 15-10771
Lenguajes de Programación I
Tarea 3
Pregunta 2.b.i
"""


import threading

# Inicializa el bloqueo
lock = threading.Lock()

def prodpunt_aux(start, end, vector1, vector2, result):
    """
    Esta función calcula una parte del producto punto.
    """
    for i in range(start, end):
        # Bloquea el acceso a la variable compartida 'result'
        with lock:
            result[0] += vector1[i] * vector2[i]

#Esta función calcula el producto punto de dos vectores utilizando múltiples hilos.
def producto_punto(vector1, vector2, num_threads):
    
    #Verificamos que tengan el mismo tamaño los vectores
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud")

    size = len(vector1)
    part = size // num_threads

    # Inicializa el resultado como una lista para permitir la mutabilidad
    result = [0]

    threads = []
    for i in range(num_threads):
        # Calcula el inicio y el fin de la parte del vector que este hilo procesará
        start = i * part
        end = size if i == num_threads - 1 else (i + 1) * part
        # Crea un nuevo hilo y lo inicia
        thread = threading.Thread(target=prodpunt_aux, args=(start, end, vector1, vector2, result))
        thread.start()
        threads.append(thread)

    # Espera a que todos los hilos terminen
    for thread in threads:
        thread.join()

    return result[0]

# Ejemplo de uso
vector1 = [1, 2, 3, 4, 5]
vector2 = [6, 7, 8, 9, 10]
num_threads = 2
print(producto_punto(vector1, vector2, num_threads))  # Imprime 130
