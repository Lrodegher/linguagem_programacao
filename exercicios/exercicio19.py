def cheese_and_crackers(cheese_count, boxes_of_crackers): #criou a função com 2 argumentos
    print(f"You have {cheese_count} cheeses!") #imprime arg1
    print(f"You have {boxes_of_crackers} boxes of crackers!") #imprime arg2
    print("Man that's enough for a party!") #imprime
    print("Get a blanket.\n") #imprime


print("We can just give the function numbers directly:") #imprime
cheese_and_crackers(20, 30) #chama a função diretamente com os valores


print("OR, we can use variables from our script:") #imprime e mostra como usar a função com combinação de variáveis
amount_of_cheese = 10 #deu o valor 1
amount_of_crackers = 50 #deu o valor 2

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #chamou o método atribuindo as variáveis aos argumentos


print("We can even do math inside too:") #imprime mostrando como usar soma para o valor dos atributos
cheese_and_crackers(10 + 20, 5 + 6) #mostra que se pode escrever a soma, separa os argumentos por VÍRGULA


print("And we can combine the two, variables and math:") #imprime e mostra a combinação de possibilidades
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #definiu os argumentos de forma mista