#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
print('   ')
from random import randint
from time import sleep
from operator import itemgetter

jogadas = {}
ranking = []

jogadas['Jogador um'] = randint(1,6)
jogadas['Jogador dois'] = randint(1,6)
jogadas['Jogador três'] = randint(1,6)
jogadas['Jogador quatro'] = randint(1,6)
print('-='*20)
print(f'{"JOGO DE DADOS":=^40}')
print('-='*20)

for n in range(0,4):
    print(f'JOGADOR {n+1} ESTÁ JOGANDO O DADO...')
    sleep(1)

print('-='*20)
for k, d in jogadas.items():
    print(f'O {k} tirou {d} no dado.')
    sleep(0.5)


ranking = sorted(jogadas.items(),key=itemgetter(1), reverse=True)

'''Função itemgetter é usada para escolhemos a chave em que queremos ordenar sejá lista, tupla ou dicionario.  No explo do exercício temos o dicionario da seguinte forma para ordenamos na ordem do maior para o menor porém está da seguinte forma, "jogador um = 5" no caso são duas chaves, o itemgetter vai escolher a chave que desejá usar dentro do sorted.'''

print('-='*20)
print('   === RANKING DOS JOGADORES')

for j , d in enumerate(ranking):
    print(f'{j+1}º lugar: {d[0]} com {d[1]}.')
    sleep(0.5)
    
print('-='*20)