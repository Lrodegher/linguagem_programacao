# Passo 1: Importar o módulo math.
import math

def adicionar(n1, n2):
    """Retorna a soma de dois números."""
    return n1 + n2

def subtrair(n1, n2):
    """Retorna a diferença entre dois números."""
    return n1 - n2

def multiplicar(n1, n2):
    """Retorna o produto de dois números."""
    return n1 * n2

def dividir(n1, n2):
    """Retorna o quociente da divisão de dois números."""
    return n1 / n2

# Passo 2: Implementar funções para cálculos de potenciação, radiciação, trigonometria e logaritmos.
def potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return math.pow(base, expoente)

def radiciacao(numero, raiz):
    """Retorna a raiz de um número."""
    if numero < 0 and raiz % 2 == 0:
        raise ValueError("Raiz par de número negativo não é real.")
    return math.pow(numero, 1/raiz)

def seno(angulo_graus):
    """Retorna o seno de um ângulo em graus."""
    return math.sin(math.radians(angulo_graus))

def cosseno(angulo_graus):
    """Retorna o cosseno de um ângulo em graus."""
    return math.cos(math.radians(angulo_graus))

def tangente(angulo_graus):
    """Retorna a tangente de um ângulo em graus."""
    return math.tan(math.radians(angulo_graus))

def logaritmo(numero, base):
    """Retorna o logaritmo de um número na base especificada."""
    if numero <= 0 or base <= 0 or base == 1:
        raise ValeuError("Número deve ser positivo e base positiva diferente de 1.")
    return math.log(numero, base)

try:
    num1_str = input("Digite o primeiro número: ")
    operador = input("Digite o operador (+, -, *, /, **, rad, sen, cos, tan, log): ")
    num2_str = input("Digite o segundo número (ou raiz/expoente/base para outras operações): ")

    # Passo 1: Verificar se os números inseridos são válidos.
    if not num1_str.replace('.', '', 1).isdigit() or not num2_str.replace('.', '', 1).isdigit():
        raise ValueError("Por favor, insira números válidos.")
    else:
        num1 = float(num1_str)
        num2 = float(num2_str)
        resultado = None

        # Passo 2: Verificar se o operador inserido é válido.
        if operador in ['+', '-', '*', '/', '**', 'rad', 'sen', 'cos', 'tan', 'log',]:
            # Passo 3: Integrar as novas funções ao programa.
            if operador == '+':
                resultado = adicionar(num1, num2)
            elif operador == '-':
                resultado = subtrair(num1 , num2)
            elif operador == '*':
                resultado = multiplicar(num1, num2)
            elif operador == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Não é possível dividir por zero.")
                else:
                    resultado = dividir(num1, num2)
            elif operador == '**':
                resultado = potencia(num1, num2)
            elif operador == 'rad':
                resultado = radiciacao(num1, num2)
            elif operador == 'sen':
                resultado = seno(num1) # Assume que o primeiro número é o ângulo em graus
            elif operador == 'cos':
                resultado = cosseno(num1) # Assume que o primeiro número é o ângulo em graus
            elif operador == 'tan':
                resultado = tangente(num1) # Assume que o primeiro número é o ângulo em graus
            elif operador == 'log':
                resultado = logaritmo(num1, num2)

            # Passo 5: Exibir o resultado.
            print(f"O resultado é: {resultado}")
        else:
            # Passo 3: Exibir mensagens de erro apropriadas.
            raise ValueError("Operador inválido. Use +, -, *, /, **, rad, sen, cos, tan, log.")

except ValueError as e:
    print(f"Erro: {e}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")