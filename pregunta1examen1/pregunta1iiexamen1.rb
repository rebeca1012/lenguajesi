#Alumno: Rebeca Ledesma
#Carnet: 15-10771
#Exámen 1
#Pregunta 1.b.ii

#Función que recibe una matriz cuadrada a y que calcula su transpuesta,
#para luego calcular la multiplicación de la matriz con su transpuesta
#Devuelve el resultado de la multiplicación

def multiplicacion(a)
    

    #Guarda el tamaño de la matriz a
    size = a.length

    #Crear matriz para alojar la transpuesta de A
    at = Array.new(size) { Array.new(size) { 0 } }

    #Calcular la transpuesta de A
    for i in (0...a.size)
        for j in (0...a[i].length)
         at[i][j] = a[j][i]
         at[j][i] = a[i][j]
        end
    end
    
    #Crear matriz para alojar el resultado de a*at
    result = Array.new(size) { Array.new(size) { 0 } }
    
    #Calcular la multiplicación de a*at
    (0...size).each do |i|
        (0...size).each do |j| 
            sum = 0
            (0...size).each do |k|
                sum += a[i][k] * at[k][j]
            end    
            result[i][j] = sum   
        end
    end
    #Retornar resultado
    return result
end

