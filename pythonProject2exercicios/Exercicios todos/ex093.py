#Exercício Python 088:
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from time import sleep
from random import randint
print('='*60)
print('='*60)
print(f'{" MEGA SENA ":=^60}')
print('='*60)
print('='*60)
quant = 0
j = int(input('Quantos jogos deseja criar para a mega ?  '))
lista = []
jogos = []
while quant != j:

    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)

        if len(lista) >= 6:
            break
    quant += 1
    jogos.append(lista[:])
    lista.clear()

print('='*60)
print(F'{" SORTEANDO JOGOS ":=^60}')
print('='*60)

for q , i in enumerate(jogos):
    print(f'JOGO  {q+1}: {i}')
    sleep(1)
