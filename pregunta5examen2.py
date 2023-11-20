#Alumno: Rebeca Ledesma
#Carnet: 15-10771
#Exámen 2
#Pregunta 5

#Clase para manejar los tipos de datos atómicos
#Cuenta con nombre, representación y alienación
class TipoAt:
    def __init__(self, nombre, representacion, alineacion):
        self.nombre = nombre
        self.representacion = representacion
        self.alineacion = alineacion

#Clase para manejar los Struct
class Struct:
    def __init__(self, nombre, tipos):
        self.nombre = nombre
        self.tipos = tipos
        


#Creamos un manejador de tipos
class ManejadorTipos:
    def __init__(self):
        self.tipos = {}

    def agregar_atomico(self, nombre, representacion, alineacion):
        if nombre in self.tipos:
            print(f"Error: El tipo '{nombre}' ya existe.")
            return 
        else:
            self.tipos[nombre] = TipoAt(nombre, representacion, alineacion)

#Función main
def main():
    manejador = ManejadorTipos()
    corriendo = True

    while corriendo:
        inputuser = input("Ingrese una instrucción: ")

        #Convertimos el input del user en una lista
        inputuser_list = inputuser.split()
        

        if inputuser_list[0] == "ATOMICO":
           manejador.agregar_atomico(inputuser_list[1], int(inputuser_list[2]), int(inputuser_list[3]))
        elif inputuser_list[0] == "STRUCT":
            pass
        elif inputuser_list[0] == "UNION":
            pass
        elif inputuser_list[0] == "DESCRIBIR":
            pass
        elif inputuser_list[0] ==  "SALIR":
            #Termina programa
            corriendo = False
        
main()