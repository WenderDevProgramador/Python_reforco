#Exercício Python 091:
# Crie um programa onde 4 jogadores
# joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'JOGADOR 1 ': randint(1,6),
             'JOGADOR 2 ': randint(1,6),
             'JOGADOR 3 ': randint(1,6),
             'JOGADOR 4 ': randint(1,6)}
for j , d in jogadores.items():
    print(f'O jogador {j} tirou {d} no dado.')
    sleep(1)
print('-='*20)
ranking = {}
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)

print('__--'*10)
print(' == RANKING DE JOGADORES == ')
for j, d in enumerate(ranking):
    print(f'{j+1}º {d[0]} tirou {d[1]} no dado!')
    sleep(1)