#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('   ')

print('--'*30)
print('{:^60}'.format('PALPITES DE JOGOS PARA MEGA SENA'))
print('--'*30)


cont = 0

jogos = int(input('Quantos jogos você quer gerar: '))
print('Gerando jogos. . .')
sleep(2)
print('   ')
while cont < jogos:
    num = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    print(f'JOGO  {cont+1}: {num}')
    sleep(0.3)
    cont += 1
print('   ')