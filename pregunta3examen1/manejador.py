#Alumno: Rebeca Ledesma
#Carnet: 15-10771
#Exámen 1
#Pregunta 3: Buddy System

from math import log2, floor, ceil

class Manejador:

    def __init__(self, bloques):

        potencia = ceil(log2(bloques))

        #Se almacenarán los bloques libres en una lista de listas
        lista_bloques = [[]]

        #LLenamos la lista hasta la potencia máxima
        for bloque in range(potencia):
            lista_bloques += [[]]
        
        self.bloques = bloques
        self.lista_bloques = lista_bloques

        #Usamos un set para almacenar los nombres y de esa manera evitar
        #repeticiones
        self.nombres = {}


    #Función donde se implementa la reserva de
    #memoria
    #Parámetros:
    #   cant: es un entero (int) que representa la cantidad
    #   de bloques a reservar
    #   nombre: (string) es el identificador asociado a los bloques
    def reservar(self, cant, nombre):
        lista_bloques = self.lista_bloques