import datetime

# Variáveis globais
saldo = 2860.00  # Saldo inicial
extrato = [
    {"data": "14/05/2025 18:19:45", "operacao": "Depósito", "valor": 1500.00},
    {"data": "14/05/2025 18:19:53", "operacao": "Depósito", "valor": 500.00},
    {"data": "14/05/2025 18:21:38", "operacao": "Saque", "valor": -150.00},
    {"data": "14/05/2025 18:21:54", "operacao": "Depósito", "valor": 10.00}
]

# Função para obter data e hora atual
def data_hora_atual():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Função para exibir o extrato
def exibir_extrato():
    print("\n--- Extrato Bancário ---")
    for movimento in extrato:
        tipo = movimento["operacao"]
        valor = movimento["valor"]
        print(f"{movimento['data']} - {tipo}: R$ {valor:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}\n")

# Função para consultar saldo
def consultar_saldo():
    print(f"\nSaldo atual: R$ {saldo:.2f}\n")

# Função para depositar
def depositar():
    global saldo
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor <= 0:
            print("Valor inválido para depósito.\n")
            return
        saldo += valor
        extrato.append({"data": data_hora_atual(), "operacao": "Depósito", "valor": valor})
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.\n")
    except ValueError:
        print("Entrada inválida. Use apenas números.\n")

# Função para sacar
def sacar():
    global saldo
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= 0:
            print("Valor inválido para saque.\n")
            return
        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.\n")
            return
        saldo -= valor
        extrato.append({"data": data_hora_atual(), "operacao": "Saque", "valor": -valor})
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
    except ValueError:
        print("Entrada inválida. Use apenas números.\n")

# Função para transferir
def transferir():
    global saldo
    conta_destino = input("Digite o número da conta do destinatário: ")
    try:
        valor = float(input("Digite o valor a transferir: R$ "))
        if valor <= 0:
            print("Valor inválido para transferência.\n")
            return
        if valor > saldo:
            print("Saldo insuficiente para realizar a transferência.\n")
            return
        saldo -= valor
        extrato.append({"data": data_hora_atual(), "operacao": "Transferência", "valor": -valor})
        print(f"\nTransferência de R$ {valor:.2f} realizada com sucesso para a conta {conta_destino}.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}\n")
    except ValueError:
        print("Entrada inválida. Use apenas números.\n")

# Função principal de menu
def menu():
    while True:
        print("--- Bem-vindo ao seu banco virtual ---")
        print("1 - Consultar Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Exibir Extrato")
        print("5 - Transferir")
        print("6 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            exibir_extrato()
        elif opcao == "5":
            transferir()
        elif opcao == "6":
            print("Obrigado por usar nosso sistema bancário. Saindo...\n")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Iniciar o sistema
menu()
