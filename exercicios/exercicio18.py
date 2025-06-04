def print_two(*args): #criou o método print_two; o asterisco é para ele puxar os argumentos conforme explicados na linha 2
  arg1, arg2 = args #disse pro código que 'arg1' e 'arg2' são os argumentos desse método, sem precisar já escrever no parêntesis
  print(f"arg1: {arg1}, arg2: {arg2}") #vai imprimir os argumentos conforme adicionados ao chamar o método

def print_two_again(arg1, arg2): #criou o método print_two_again
  print(f"arg1: {arg1}, arg2: {arg2}") #se entregar argumentos diferentes para esse método, ele não vai alterar os argumentos do método print_two

def print_one(arg1): #criou o método print_one
  print(f"arg1: {arg1}") #vai imprimir o argumento disponível para o print_one

def print_none(): #definiu o método print_none, que não pede argumentos
  print("I got nothyin'.") #imprime

print_two("Zed", "Shaw") #chama o método, definindo os argumentos
print_two_again("Bibi", "Frufru")#chama o método, definindo os argumentos - alterado do código original para teste
print_one("First!")#chama o método, definindo os argumentos
print_none()#chama o método, definindo os argumentos