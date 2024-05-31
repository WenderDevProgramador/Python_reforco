'''Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
print(input('Aperte qualquer tecla para iniciar a contagem regreciva para o ano novo!! : '))
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('\033[1;34m {:=^70}'.format(' FELIZ ANO NOVO !! '))
