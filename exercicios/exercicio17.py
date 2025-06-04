i = 0 #deu o valor inicial do elemento (i) ##os comentários são inseridos apenas lendo o teste, sem rodar, e alterados se necessário depois do teste.
numbers = [] #criou a lista numbers

while i < 6: #criou um laço que vai atuar enquanto o (i) for menor que 6
  print(f"This is cycle #{i + 1}") #acrescentei essa linha pra usar o i como noção das repetições do loop
  print(f"At the top i is {i}") #deve imprimir que o valor do i conforme o loop é executado
  numbers.append(i) #acrescenta esse valor de i à lista numbers

  i = i + 1 #soma 1 ao valor do i que o código acabou de usar no loop
  print("Number now: ", numbers) #ele vai imprimir a lista inteira disponível na etapa do ciclo while
  print(f"At the bottom i is {i}") #deve imprimir o valor mais recente de i após a soma

print("The numbers: ") #só imprime a frase
for num in numbers: #vai chamar cada elemento (num) da lista numbers
  print(num) #imprime cada um desses elementos)