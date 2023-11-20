#Alumno: Rebeca Ledesma
#Carnet: 15-10771
#Exámen 2
#Pregunta 2

# El módulo operator proporciona funciones equivalentes a los operadores intrínsecos de Python. 
# Por ejemplo, operator.add(x, y) es equivalente a la expresión x + y.

import operator 
import sys

# Diccionario para mapear los símbolos a las funciones del módulo operator
operations = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

# Implementación de una pila para ir agregando los elementos de la expresion dada

class Stack:
    # Crea la pila
    def __init__(self):
        self.elementos = []
    
    # Push elements
    def push(self, item):
        self.elementos.append(item)

    # Muestra el tope de la pila
    def top(self):
      return self.elementos[-1]
    
    # Quita el elemento actual de la pila
    def pop(self):
        if (self.size() == 0):
            raise "La pila está vacía!"
        else:
            return self.elementos.pop()
    
    # Si la pila está vacía, retorna true
    def isEmpty(self):
      if self.size() == 0:
        return True

    # Muestra el tamaño de la pila
    def size(self):
        return len(self.elementos)
    
    # Muestra la pila
    def display(self):
        print(self.elementos)
        return
   

# Recibe un caracter y determina si es un número
def esOperando(char):
  if char.isnumeric():
    return True

# Recibe un caracter y determina si es un operador
def esOperador(char):
  if char in "+-/*":
    return True

# Recibe dos operadores y se encarga de determinar
# cuál de los dos tiene mayor precedencia
def tienePrecedencia(op1, op2):
  # Asignamos la precedencia de cada uno de los operadores
  # con un diccionario
  precedencia = {'+':1, '-':1, '*':2, '/':2}
  # Prevenir error de llave equivocada
  try: 
    prec_op1 = precedencia[op1]
    prec_op2 = precedencia[op2]
    
    if prec_op1 >= prec_op2:
      return True
    return False

  except KeyError:
    return False

# Implementación de clase 
class Postfija:
  def __init__(self, expresion:list):
    self.expresion = expresion
    self.precedencia = {'+':1, '-':1, '*':2, '/':2}

  """
  Este método evalúa la expresión postfija almacenada en la instancia de la clase.
  Utiliza una pila para almacenar los operandos y realiza las operaciones en el orden correcto.
  Si encuentra un error durante la evaluación (por ejemplo, si la expresión contiene un operador no válido o
  si hay más operadores que operandos), devuelve un mensaje de error.
  """
  def evaluar(self):
    expresion = self.expresion
    stack = Stack()
    result = 0

    try:
      for i in range(len(expresion)):

        if esOperando(expresion[i]):
          stack.push(expresion[i])
      
        elif esOperador(expresion[i]):
          op1 = int(stack.top())
          stack.pop()
          op2 = int(stack.top())
          stack.pop()
          res = operations[expresion[i]](op2, op1)
          stack.push(res)
        
      while not stack.isEmpty():
        result += stack.top()
        stack.pop()
      
      #Retorna el resultado
      return result
    
    except:
      return 'Error! La expresión que ingresaste no es válida. Inténtalo otra vez.'

  
  #Convierte una expresión Postfija a la notación Infija
  def aInfija(self):
      stack = Stack()

      try:
          for i in range(len(self.expresion)):

              if esOperando(self.expresion[i]):
                  stack.push(self.expresion[i])

              elif esOperador(self.expresion[i]):
                  op2 = stack.top()
                  stack.pop()
                  op1 = stack.top()
                  stack.pop()
                  res = '(' + op1 + self.expresion[i] + op2 + ')'
                  stack.push(res)

          # Retorna el resultado
          return stack.top()

      except:
          return 'Error! La expresión que ingresaste no es válida. Inténtalo otra vez.'


class Prefija:
  def __init__(self, expresion: list):
    self.expresion = expresion

  def evaluar(self):
    # Voltea la lista
    expresion = self.expresion[::-1] 
    stack = Stack()
    result = 0

    try:
      for i in range(len(expresion)):

        if esOperando(expresion[i]):
          stack.push(expresion[i])
      
        elif esOperador(expresion[i]):
          op1 = int(stack.top())
          stack.pop()
          op2 = int(stack.top())
          stack.pop()
          res = operations[expresion[i]](op1, op2)
          stack.push(res)
        
      while not stack.isEmpty():
        result += stack.top()
        stack.pop()
      
      #Retorna el resultado
      return result
    
    except:
      return 'Error! La expresión que ingresaste no es válida. Inténtalo otra vez.'
    
  def aInfija(self):
      # Voltea la lista
      expresion = self.expresion[::-1]
      stack = Stack()

      try:
          for i in range(len(expresion)):

              if esOperando(expresion[i]):
                  stack.push(expresion[i])

              elif esOperador(expresion[i]):
                  op1 = stack.top()
                  stack.pop()
                  op2 = stack.top()
                  stack.pop()
                  res = '(' + op1 + expresion[i] + op2 + ')'
                  stack.push(res)

          # Retorna el resultado
          return stack.top()

      except:
          return 'Error! La expresión que ingresaste no es válida. Inténtalo otra vez.'    
    

def notacion(expresion):
    if esOperador(expresion[0]):
        return 'Prefija'
    elif esOperador(expresion[-1]):
        return 'Postfija'
    else:
        return 'La expresión no es ni prefija ni postfija'

def main():
    corriendo = True
    while corriendo:
        inputuser = input("Ingrese una acción en el formato INSTRUCCIÓN <orden> <expr>:  ")
        
        #Convertimos el input del user en una lista
        inputuser_list = inputuser.split()
        

        #Verificar cuál es la instrucción que se quiere

        if inputuser_list[0] == "EVAL" or inputuser_list[0].upper() == "EVAL":
          if inputuser_list[1] == "PRE" or inputuser_list[1].upper() == "PRE":
            exp = inputuser_list[2:len(inputuser_list)]
            _expresion = Prefija(exp)
            print()
            print("La expresión prefija es:", inputuser[9:len(inputuser)])
            print("Respuesta:", _expresion.evaluar())
            print() 
          elif inputuser_list[1] == "POST" or inputuser_list[1].upper() == "POST":
            exp = inputuser_list[2:len(inputuser_list)]
            _expresion = Postfija(exp)
            print()
            print("La expresión postfija es:", inputuser[10:len(inputuser)])
            print("Respuesta:", _expresion.evaluar())
            print()
          else:
            print("Instrucción equivocada. Intente otra vez!")
            continue     
          
        elif inputuser_list[0] == "MOSTRAR" or inputuser_list[0].upper() == "MOSTRAR" :
          exp = inputuser_list[1:len(inputuser_list)]
          print(exp)
          #Definir si la expresión es prefija o postfija
          tipo = notacion(exp)

          if tipo == "Prefija":
            p = Prefija(exp)
            # Convertir la expresión a notación infija
            infija = p.aInfija()
            print(infija)  
          elif tipo == "Postfija":
            p = Postfija(exp)
            # Convertir la expresión a notación postfija
            infija = p.aInfija()
            print(infija)  
          #acá se debe mostrar lo que quiere el user
        elif inputuser_list[0] == "SALIR" or inputuser_list[0].upper() == "SALIR":
          #Termina el programa
          corriendo = False
        else:
          print("Instrucción equivocada. Intente otra vez!")
          continue

if __name__ == '__main__':
  main()