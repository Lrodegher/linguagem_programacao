
import time

def openLog(nomearq, modo = 'r'):
    arqEntrada = open(nomearq, modo)

    now = time.localtime()
    nowFormat = time.strftime('%A %b/%d/%y %I:%M %p', now)

    arqSaída = open('lucas_santos.txt' , 'a')
    log = '{}: Arquivo {} aberto.\n'
    arqSaída.write(log.format(nowFormat, nomearq))
    arqSaída.close()

    print('Registro realizado')

    return arqEntrada