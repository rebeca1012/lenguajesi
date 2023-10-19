"""
Alumno: Rebeca Ledesma
Carnet: 15-10771
Exámen 1
Pregunta 4: Módulo de vectores 3D
"""

import math
from numbers import Real

#Creación de la clase Vector
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    #Definición de la suma entre vectores, representada por +
    #Lo que hacemos es reimplementar el operador +. Y hacemos lo mismo
    #para los demás operadores
    def __add__(self, nvector):
        #Verificamos si el input es un vector y un real, o dos vectores para determinar qué operación hacer
        #De esta forma también nos aseguramos que solo se permitan las operaciones por la derecha
        if isinstance(nvector, Real):
            # Suma de un vector y un escalar
            return Vector(self.x + nvector, self.y + nvector, self.z + nvector)
        else:
            # Suma de vectores
            return Vector(self.x + nvector.x, self.y + nvector.y, self.z + nvector.z)
    
    def __sub__(self, nvector):
        if isinstance(nvector, Real):
            # Resta de un vector y un escalar
            return Vector(self.x - nvector, self.y - nvector, self.z - nvector)
        else:
            # Resta de vectores
            return Vector(self.x - nvector.x, self.y - nvector.y, self.z - nvector.z)
    
    def __mul__(self, nvector):
        if isinstance(nvector, (Real)):
            # Producto cruz de un escalar y un vector
            return Vector(nvector * self.y - nvector * self.z,
                          nvector * self.z - nvector * self.x,
                          nvector * self.x - nvector * self.y)
        else:
            # Producto cruz de vectores
            return Vector(self.y * nvector.z - self.z * nvector.y,
                          self.z * nvector.x - self.x * nvector.z,
                          self.x * nvector.y - self.y * nvector.x)
    
    def __mod__(self, nvector):
        # Producto punto de vectores
        return self.x * nvector.x + self.y * nvector.y + self.z * nvector.z
    
    #Se tuvo que definir como método y no sobrecarga porque Python no permite
    #cambiar un símbolo binario a unario
    def norma(self):
        # Norma de un vector
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __str__(self):
        # Mostrar vector como string
        return f"({self.x}, {self.y}, {self.z})"
