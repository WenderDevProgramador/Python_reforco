#Exercício Python 100:
# Faça um programa que tenha uma lista
# chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia(list):
    for s in range(0,5):
        list.append(randint(1,10))
    print(f'Os números sorteados são {list} .')


def sortpar(list):
    cont = 0
    for v in list:
        if v % 2 == 0:
            cont += v
    print(f'O resultado da soma dos números pares são {cont} .')


números = []

sorteia(números)
sortpar(números)
print(números)







