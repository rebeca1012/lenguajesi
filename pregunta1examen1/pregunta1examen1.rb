#Alumno: Rebeca Ledesma
#Carnet: 15-10771
#Exámen 1
#Pregunta 1.b.i

#Función que recibe una palabra (string) y un número k que va a ser 
#la cantidad de rotaciones a aplicar a la palabra. 
#Retorna la palabra resultante de hacer las rotaciones

def rotar(palabra, k)
    #Cuando queda igual es cuando k es cero, cuando k es un múltiplo del tamaño 
    #de la palabra o cuando k es del tamaño de palabra
    if k == 0 || k % palabra.length == 0
        return palabra
    else
        #Como los procedimientos se repiten si k es mayor que el tamaño de la palabra
        #hagamos mod para que se haga el procedimiento una sola vez dentro del rango
        #del tamaño de la palabra
        rep = (k % palabra.length) #rep es la cantidad de repeticiones, nuestro nuevo k
        
        final = palabra[0,rep] #final es la parte final de palabra que vamos a imprimir

        inicio = palabra[rep..] #inicio es la parte inicial de la palabra que vamos a imprimir
        
        return inicio + final
    end    
end

