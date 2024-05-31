#Exercício Python 074:
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

núm = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
for n in núm:
    print(n, end=' ')
print(f'\nOs números gerados são {núm} .')
print(f'O menor valor é {min(núm)} e o maior valor é {max(núm)} .')

