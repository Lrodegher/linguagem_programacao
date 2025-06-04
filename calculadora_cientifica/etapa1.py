# passo 1: solicitar ao usuário que insira os números e a operação
numero1 = float(input("digite o primeiro número: "))
operador = (input("digite o operador (+, -, *, /): "))
numero2 = float(input("digite o segundo número: "))


# passo2: realizar a operação correspondente
if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    resultado = numero1 / numero2
else:
    resultado = "operador inválido"

# passo 3: exibir o resultado
print("resultado:", resultado)