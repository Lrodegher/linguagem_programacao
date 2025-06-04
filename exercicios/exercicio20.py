def add(a, b): #criou a função com a operação
  print(f"ADDING {a} + {b}") #imprime que está somando
  return a + b #salva o valor

def subtract(a, b): #criou a função subtract
  print(f"SUBTRACTING {a} - {b}") #vai imprimir a subtração de a - b
  return a - b #salva o valor

def multiply(a, b): #criou a função com a operação
  print(f"MULTIPLYING {a} * {b}") #imprime que está somando
  return a * b #salva o valor

def divide(a, b):#criou a função com a operação
  print(f"DIVIDING {a} / {b}") #imprime que está somando
  return a / b  #salva o valor

print("Let's do some more math with just functions!") #só imprime

age = add(30, 5) #puxa o método com os valores definidos para aplicar
height = subtract(78, 4) #puxa o método com os valores definidos para aplicar
weight = multiply(90, 2) #puxa o método com os valores definidos para aplicar
iq = divide(100, 2) #puxa o método com os valores definidos para aplicar

print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}") #vai puxar as respostas todas salvas

#Charada extra:
print("Here is a puzzle.") #só mprime
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#iq = 50; add(age, subtract(height, multiply(weight, divide(50, 2))))
#divide(50, 2) = 25; add(age, subtract(height, multiply(weight, 25)))
#multiply(weight, 25) // weight = 90*2 = 180 // multiply(180, 25) = 4500 // add(age, subtract(height, 4500))
#subtract(height, 4500) = 74-4500 = 4426 // add(age, 4426)
#add(35, 4426) = 4461 UÉ???
print("That becomes: ", what, "Can you do it by hand?")