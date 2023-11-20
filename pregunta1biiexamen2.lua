[[--
Alumno: Rebeca Ledesma
Carnet: 15-10771
Exámen 2
Pregunta 1.b.ii
--]]

-- Definición de la estructura de nodo
Nodo = {}
function Nodo:nuevo(valor)
  local nodo = {}
  nodo.valor = valor
  nodo.izquierda = nil
  nodo.derecha = nil
  return nodo
end

-- Función para recorrer el árbol en pre-orden
function preOrden(nodo, secuencia)
  if nodo then
    table.insert(secuencia, nodo.valor)
    preOrden(nodo.izquierda, secuencia)
    preOrden(nodo.derecha, secuencia)
  end
end

-- Función para recorrer el árbol en post-orden
function postOrden(nodo, secuencia)
  if nodo then
    postOrden(nodo.izquierda, secuencia)
    postOrden(nodo.derecha, secuencia)
    table.insert(secuencia, nodo.valor)
  end
end

-- Función para verificar si es un max-heap simétrico
function esMaxHeapSimetrico(raiz)
  local preOrdenSecuencia = {}
  local postOrdenSecuencia = {}

  -- Obtener secuencia en pre-orden
  io.write("Secuencia en pre-orden: ")
  preOrden(raiz, preOrdenSecuencia)
  for i, v in ipairs(preOrdenSecuencia) do
    io.write(v .. " ")
  end
  io.write("\n")

  -- Obtener secuencia en post-orden
  io.write("Secuencia en post-orden: ")
  postOrden(raiz, postOrdenSecuencia)
  for i, v in ipairs(postOrdenSecuencia) do
    io.write(v .. " ")
  end
  io.write("\n")

  -- Comparar las secuencias resultantes y determinar si es simétrico o no
  for i = 1, #preOrdenSecuencia do
    if preOrdenSecuencia[i] ~= postOrdenSecuencia[#postOrdenSecuencia - i + 1] then
        print("No es un max-heap simétrico")
      return false
    end
  end
  print("Es un max-heap simétrico")
  return true
end



-- Construcción del árbol binario
raiz = Nodo:nuevo(10)
raiz.izquierda = Nodo:nuevo(5)
raiz.derecha = Nodo:nuevo(15)
raiz.izquierda.izquierda = Nodo:nuevo(3)
raiz.izquierda.derecha = Nodo:nuevo(8)
raiz.derecha.izquierda = Nodo:nuevo(12)
raiz.derecha.derecha = Nodo:nuevo(20)


-- Construcción de otro árbol binario

raiz2 = Nodo:nuevo(10)
raiz2.izquierda = Nodo:nuevo(2)
raiz2.derecha = Nodo:nuevo(2)

-- Verificar si el árbol es un max-heap simétrico

esMaxHeapSimetrico(raiz)
esMaxHeapSimetrico(raiz2)
