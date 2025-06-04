the_count = [1, 2, 3, 4, 5] #cria lista the_count
fruits = ['apples', 'oranges', 'pears', 'apricots'] #cria lista fruits
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] #cria lista change

for number in the_count: #para cada elemento dentro de the_count, que chamei de number, ele:
  print(f"This is count {number}") #imprime cada elemento

for fruit in fruits: #para cada elemento dentro de fruits, que chamei de fruit, ele:
  print(f"A fruit of type: {fruit}") #imprime cada elemento

for i in change: #para cada elemento dentro de change, identificado pelo padrão i, ele:
  print(f"I got {i}") #imprime cada elemento

elements = [] #cria a lista elements

for i in range(0, 6): #vai considerar 6 elementos, contando em números a partir do zero
  print(f"Adding {i} to the list.") #imprime que adicionou os elementos à lista elements

  elements.append(i) #essa liha é para de fato adicionar esses 5 elementos à lista element (notar tabulação dentro do for)

for i in elements: #busca o item dentro da lista elements
  print(f"Element was: {i}") #imprime o item