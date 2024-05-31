#Exercício Python 098:
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print(f' Contando de {i} até {f} em {p}: ')
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            sleep(0.3)
            cont += p
        print('Fim. . .')
        print('-=' * 30)
    else:
        print(f' Contando de {i} até {f} em {p}: ')
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            sleep(0.3)
            cont -= p
        print('Fim. . .')
        print('-=' * 30)



contador(1,10,1)
contador(10,0,2)
print('-='*30)
print(f'{"AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM:":=^}')
i = int(input('Nº inicial : '))
f = int(input('Nº final: '))
p = int(input('Nº de contagem: '))
contador(i,f,p)