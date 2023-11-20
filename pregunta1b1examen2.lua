[[--
Alumno: Rebeca Ledesma
Carnet: 15-10771
Exámen 2
Pregunta 1.b.i
--]]

-- Definición del cero
-- Recibe una función f
function cero(f)
    return function(x)
        -- Devuelve x sin cambios
        return x
    end
end

-- Definición de la función sucesor
-- Recibe un número n
function sucesor(n)
    return function(f)
        return function(x)
            -- Aplica la función f a x, n veces. Y luego
            -- aplica f una vez más. Esto simula incrementar el 
            -- número n en 1.
            return f(n(f)(x))
        end
    end
end

-- Definición de la función suma
-- Recibe dos números m y n
function suma(m, n)
    return function(f)
        return function(x)
            -- Aplica la función f al resultado m veces,
            -- para sumar m y n.
            return m(f)(n(f)(x))
        end
    end
end

-- Definición de la función multiplicación
-- Recibe dos números m y n
function multiplicacion(m, n)
    return function(f)
        return function(x)
            -- Aplica la función f a x, n veces. Y luego
            -- aplica la función resultante m veces, para
            -- multiplicar los números m y n.
            return m(n(f))(x)
        end
    end
end


-- Definición de uno y dos usando la función sucesor
uno = sucesor(cero)
dos = sucesor(uno)

-- Prueba de la función suma
tres = suma(uno, dos)
print(tres(function(x) return x + 1 end)(0)) 

-- Prueba de la función multiplicación
cuatro = multiplicacion(dos, dos)
print(cuatro(function(x) return x + 1 end)(0))