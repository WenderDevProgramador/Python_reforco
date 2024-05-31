#Exercício Python 106:
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.

def ajuda(msg):
    '''
    -->   Consulta do manual de funções:
    :param msg: Digite a função para consulta.
    :return: Retorna com o manual da função.
    '''
    from time import sleep
    print(f'Acessando o manual do {msg}: ')
    sleep(1)
    print('\033[0;30;43m', end='')
    help(msg)
    return help(msg)



def titulo(msg, cor=0):
    '''
    -->    Estilização de titulos...
    :param msg: Digite o titulo para estilizar.
    :param cor: Digite a cor para o fundo do titulo(você tem acesso as cores no manual da função).
    :return: Retorna com o titulo estilizado.
    '''
    from time import sleep
    c = ('\033[m',  # 0 - sem cor
         '\033[0;30;41m',  # 1 - vermelho
         '\033[0;30;42m',  # 2 - verde
         '\033[0;30;43m',  # 3 - amarelo
         '\033[0;30;44m',  # 4 - azul
         '\033[0;30;45m',  # 5 - roxo
         '\033[7;30m')  # 6 - branco
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg:^}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1.5)



while True:
    titulo('SISTEMA AJUDA pyHELP',4)
    comando = str(input('Metodo ou função para consultar > [FIM para finalizar]: ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        titulo('ACESSANDO METODO OU FUNÇÃO >',2)
        titulo(comando,4)
        ajuda(comando)
titulo('ATE LOGO',1)

