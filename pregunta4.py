"""
Alumno: Rebeca Ledesma
Carné: 15-10771
Lenguajes de Programación I
Tarea 3
Pregunta 4

"""

from typing import Tuple, List, Dict


#Función para crear las clases. Recibe el diccionario de las clases y el input deseado
def crear_clase(clases, datos):
    if len(datos) < 1:
        print("Invalid number of datoseters")
        return
    
    #Guardamos el nombre de la clase y lo eliminamos del input dado
    nombre = datos[0]
    del datos[0]

    #Buscamos el nombre de la clase en el dictionario para ver si ya existe
    if nombre in clases.keys():
        print("La clase ya existe!")
        return
    
    #Chequeamos el resto del string para comprobar si la clase que se va a crear
    #hereda de otra clase
    if len(datos) > 1 and datos[0] == ":":

        #Verificamos por definiciones de métodos repetidas
        if len(datos) - 2 != len(set(datos[2:])):
            print("Definición de método repetida!")
            return
        
        #Guardamos el nombre de la super clase
        superclase = datos[1]

        #Revisamos si la superclase existe o no
        if superclase not in clases.keys():
            print("La superclase no existe!")
            return
        #Llamamos a la función métodos heredados para obtener los métodos heredados de
        #la superclase y luego guardarla
        tmp = metheredados(nombre, datos[2:], clases[superclase])
        if tmp == []:
            return
        clases[nombre] = tmp
    else:
        #Verificamos que la longitud de los argumentos sea distinta a la longitud del set de los
        #argumentos para así asegurarnos que no haya definiciones de métodos repetidas
        if len(set(datos)) != len(datos):
            print("Definición de método repetida!")
            return
        #Asigna los métodos a la clase
        clases[nombre] = [(nombre, metodo) for metodo in datos]
    print("La clase ha sido creada con éxito!")

#Función para describir las clases. Recibe el diccionario de las clases y el input deseado
def descripcion(clases, datos):
    #Verificamos que se reciba un solo dato
    if len(datos) != 1:
        print("Input inválido")
        return
    nombre_clase = datos[0]
    #Verificamos la existencia de la clase
    if nombre_clase not in clases.keys():
        print("La clase no existe!")
        return
    print("Tabla de métodos virtuales de " + nombre_clase)
    #Iteramos por los métodos de la clase y luego se imprime 
    #en el formato solicitado
    for metodo in clases[nombre_clase]:
        print(metodo[1] + " -> " + metodo[0] + " :: " + metodo[1])
    print("")

#Función para manejar los métodos hereados
def metheredados(nombre, metodos_clase, metodos_super):
    #Creamos una lista para almacenar los métodos nuevos
    metodosnuevos = []
    #Creamos una lista copia para los métodos de la super clase,
    #para no modificarla directamente
    metodos = metodos_super.copy()
    #Trackea si un método de la superclase ha sido modificado en la clase
    modified: bool = False
    for metodo in metodos_clase:
        for i in range(len(metodos)):
            if nombre == metodos_super[i][0]:
                print("Ciclo en la jerarquía de herencia!")
                return []
            if metodo == metodos_super[i][1]:
                modified = True
                #Modifica el método
                metodos[i] = (nombre, metodo)
                break
        #Si no ha sido modificado, se agrega a los métodos nuevos
        if not modified:
            metodosnuevos.append((nombre, metodo))
        modified = False

    #Combinamos los métodos
    metodos.extend(metodosnuevos)
    #Devuelve los métodos heredados y los de la clase
    return metodos

#Función main
def main():
    # Inicializamos el diccionario de clases
    clases: Dict[str, List[Tuple[str, str]]] = {} 

    while True:
        instruccion = input("Ingresa una instrucción: ")
        #Separamos la instrucción en una lista
        datos = instruccion.split()
        #Obtenemos la instrucción específica y modificamos
        #el string para que quede el resto de los datos
        inst = datos[0].lower()
        datos = datos.pop(0)
        if inst == "class":
            crear_clase(clases, datos)
        elif inst == "describir":
            descripcion(clases, datos)
        elif inst == "salir":
            print("El programa ha terminado!")
            break
        else:
            print("Ingresa una instrucción válida!")

#Llamada a main  
main()