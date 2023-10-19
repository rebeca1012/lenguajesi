"""
Alumno: Rebeca Ledesma
Carnet: 15-10771
Exámen 1
Pregunta 4: Módulo de vectores 3D, archivo de pruebas
"""

from vector import Vector

# Crear dos vectores de tres dimensiones
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Suma de vectores
v3 = v1 + v2
print(v3) # (5, 7, 9)

# Resta de vectores
v4 = v1 - v2
print(v4) # (-3, -3, -3)

# Producto cruz de vectores
v5 = v1 * v2
print(v5) # (-3, 6, -3)

# Producto punto de vectores
v6 = v1 % v2
print(v6) # 32

# Norma de un vector
v7 = Vector.norma(v1)
print(v7) # 3.7416573867739413



# Crear dos vectores de tres dimensiones
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Suma de un vector y un escalar
v3 = v2 + 3
print(v3) # (7, 8, 9)

# Multiplicación cruzada de un escalar y un vector
v4 = v1 * 3.0
print(v4) # (3.0, 6.0, 9.0)

# Suma de vectores con un producto punto en el medio
v5 = (v1 + v2) * (v2 % v1)
print(v5) # (-54.0, 108.0, -54.0)