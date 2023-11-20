#Alumno: Rebeca Ledesma
#Carnet: 15-10771
#Exámen 2
#Pregunta 3.b

# Definimos una función llamada sublistas_crecientes para crear el iterador
# Recibe una lista de enteros
def sublistas_crecientes(lst):

    #Creamos una función auxiliar que toma dos argumentos:
    # un índice i y una lista aux
    def helper(i, aux):

        #Si ya llegamos al final de lst, producimos la lista aux
        #como una sublista de lst
        if i == len(lst):
            yield aux
        #Si no se ha llegado al final, verificamos si aux está vacía
        # o si el elemento actual de lst es mayor que el último de aux.
        # De ser así, se añade el elemento actual a aux para generar otra sublista
        # creciente.
        else:
            if not aux or lst[i] > aux[-1]:
                #Llamada a helper con el sig. índice y la lista actualizada
                for sublista in helper(i + 1, aux + [lst[i]]):
                    yield sublista

            #Llamamos a helper con el sig. índice y la lista aux. Y se iteran
            # por todos los valores producidos por esta llamada a helper        
            for sublista in helper(i + 1, aux):
                yield sublista
    #Produce todas las sublistas crecientes de lst
    # Se hace la llamada con índice 0 y una lista vacía
    return helper(0, [])

# Test
for sublista in sublistas_crecientes([1, 4, 3, 2, 5]):
    print(sublista)
