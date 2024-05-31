#Exercício Python 68:
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('=='*30)
print('=='*30)
print('{:^60}'.format(' JOGO DO PAR OU IMPAR '))
print('=='*30)
print('=='*30)

v = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Escolha um número para jogar: '))
    soma = pc + jogador
    escolher = ' '
    while escolher not in 'IP':
        escolher = str(input('Você escolher impar ou par? [I/P]: ')).upper().strip()[0]
    print(f'O computador colocou {pc} e você colocou {jogador}.Você escolheu','IMPAR.'if escolher == 'I'else 'PAR.')
    print(f'A Soma dos dois valores foi {soma}.')
    if soma % 2 == 0:
        print('DEU PAR')
    elif soma % 2 != 0:
        print('DEU IMPAR')
    if escolher == 'P':
        if soma % 2 == 0:
            print('Você GANHOU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif escolher == 'I':
        if soma % 2 != 0:
            print('Você GANHOU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
print(f'GAME OVER !! Você ganhou {v} vezes.')
