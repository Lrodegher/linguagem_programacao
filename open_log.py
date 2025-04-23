import time

def openLog(nomearq, modo):
    # Abre o arquivo desejado
    arqEntrada = open(nomearq, modo)

    # Data e hora atuais formatadas
    data_hora = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())

    # Registra o acesso no log
    with open("log.txt", "a") as log:
        log.write(f"[{data_hora}] Arquivo acessado: {nomearq} (modo: {modo})\n")

    return arqEntrada

# Exemplo de uso:
# arquivo = openLog("teste.txt", "r")
# print(arquivo.read())
# arquivo.close()
