'''Jogo cara ou coroa para apostas.
Colocar opção para apóstar escolher valores.
Acumular valor até perder o saldo.
O jogo deverar ser estilo cassino, da esperança de ganho porém
tem que ser mais dificil para ser lucrativo para a casa de apóstas.
O jogo deverar criar uma pasta para cada jogador novo.
O jogo deverá ser proibido para menores de idade.
'''

from time import sleep
from random import randint
def titulo(msg,tam=42):
    print('-'*tam)
    print(f'{msg:}'.center(tam))
    print('-' * tam)


def LeiaNome(msg):
    a = str(input(msg)).strip().title()
    if a.strip() == '':
        a ='<usuario desconhecido>'
    return a

def LeiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except KeyboardInterrupt:
            print('Usuario preferiu sair...')
        except:
            print('ERRO! Digite um número inteiro valido.')
        else:
            return a
            break


def LeiaValor(msg):
    while True:
        try:
            a = float(input(msg))
            if a < 2:
                print('O valor não pode ser menor que R$ 2,00')
        except KeyboardInterrupt:
            print('Usuario preferiu sair...')
        except:
            print('ERRO! Digite um valor valido.')
        else:
            return a
            break


cadastro_de_j = {}

titulo(f'{"JOGO CARA OU COROA":=^100}',100)
print('         --> Sejá bem vindo ao jogo!!')
sleep(2)
print('A diante vamos passar as regras do jogo ...')
sleep(2)
print('''  O jogador deverá fazer um cadastro previo na plataforma.
  Gostariamos de lembrar que nossa plataforma não se responsbiliza por perdas no jogo.
  O usuario só poderá solicitar resgate de valores após ralizar no minimo 3 jogadas consecutivas.''')
sleep(3)
print('-' * 100)

while True:

    acordo = str(input('Se concorda com os termos digite SIM ou NÃO: ')).strip().upper()
    if acordo == 'NÃO':
        print('OK. Obrigado! Até a proxima...')
        break
    elif acordo not in 'SIMNÂO':
        print('Erro ! Digite uma resposta válida. ')

    else:
        titulo('ESTANDO TUDO DE ACORDO VAMOS COMEÇAR')
        print('Vamos iniciar seu cadastro...')
        sleep(2)
        print('-' * 30)
        njogador = LeiaNome('Nome: ')
        idade = LeiaInt('Idade: ')
        if idade < 18:
            print('\033[1;31mO jogo é proibido para menores de 18 anos!\033[m')
            break
    while True:
        cont = 0
        while cont != 3:
            valoraposta = 0
            while valoraposta < 2:
                valoraposta = LeiaValor('Qual será o valor da apósta? R$ ')
            cadastro_de_j['NOME'] = [njogador,idade]
            titulo('VAMOS JOGAR')
            jogador = ' '
            while jogador not in 'CARACOROA':
                jogador = str(input(f'{cadastro_de_j["NOME"][0]} você escolhe "CARA" ou "COROA" ? ')).strip().upper()
                if jogador not in 'CARACOROA':
                    print('Erro ! Você deve digitar "CARA" ou "COROA" !')
            moeda = ('CARA', 'COROA')
            sort = randint(0,1)
            lado_ganha = moeda[sort]
            titulo('JOGANDO MOEDA . . .')
            sleep(3)
            print(f'\033[1;31mDeu {lado_ganha} !! \033[m')

            caixa = valoraposta

            if jogador == lado_ganha:
                print('\033[1;31m    --> Você ganhou!!\033[m')
                caixa += caixa + valoraposta
                cont += 1
            elif jogador != lado_ganha:
                    print('\033[1;31mVOCÊ PERDEU !!!!\033[m')
                    caixa = 0
                    cont += 1
            print('-' * 30)
            print(f'O valor do seu caixa atual é de R${caixa:.2f}')
            if cont < 3:
                print(f'Jogue mais {3 - cont} vezes e poderá sacar seu saldo.')
        if cont == 3:
            titulo('\033[1;33m--> ATINGIU AS 3 JOGADAS JÁ PODE SACAR SEU PREMIO!! <--\033[m')
            break



    break
sleep(4)
titulo('Obrigado !! Volte sempre !')





