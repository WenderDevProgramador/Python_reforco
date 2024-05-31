#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from time import sleep

def sorteio(lista):
    from random import randint
    cont = 0
    while True:
        lista.append(randint(0,10))
        cont += 1
        if cont == 5:
            break
    

def somaPar(lista):
    cont = 0
    for v in lista:
        if v % 2 == 0:
            cont += v
    return cont
print('  ')    

lista = []    
sorteio(lista)

print('Sorteando 5 valores da lista: ',end=' ')
for v in lista:
    print(v,end=' ',flush=True)
    sleep(0.3)
    
print(f'\nSomando os valores PARES de {lista}, temos {somaPar(lista)}')


print('  ')