def adicionar (n1, n2):
    """Retorna a soma de dois números."""
    return n1 + n2

def subtrair (n1, n2):
    """Retorna a diferença entre dois números."""
    return n1 - n2

def multiplicar (n1, n2):
    """Retorna o produto de dois números."""
    return n1 * n2

def dividir (n1, n2):
    """Retorna o quociente da divisão de dois números."""
    return n1 / n2


num1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador logico (+, -, *, /): ")
num2 = float(input("Digite o segundo numero: "))


if (operador == '+'):
    resultado = adicionar(num1, num2)
elif (operador == '-'):
    resultado = subtrair(num1, num2)
elif (operador == '*'):
    resultado = multiplicar(num1, num2)
elif (operador == '/'):
    resultado = dividir(num1, num2)
else:
    print("Operador invalido!")
    resultado = None

if (resultado is not None):
    print(f"O resultado e: {resultado}")