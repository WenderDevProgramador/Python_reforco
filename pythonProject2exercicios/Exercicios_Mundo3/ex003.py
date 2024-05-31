#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso mostre a listagem gerada e indique o maior e o menor número da tupla. 

from time import sleep
from random import randint

print('==>   Sorteando números. . . ')
sleep(2)

num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Segue números sorteados:',end=' ')
for n in num:
    print(n, end=' ')
print('  ')
print(f'\nO maior número da tupla é {max(num)}.')
print(f'O menor número da tupla é {min(num)}.')