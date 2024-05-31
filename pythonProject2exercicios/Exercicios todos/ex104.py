'''Exercício Python 099:
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(*num):

    print('-=' * 30)
    print(f'Analisando valores,',end=' ')
    sleep(0.3)
    if 0 in num and len(num) == 1:
        print('\nAqui temos apenas o número zero.')
    elif len(num) == 0:
        print('\nNão temos valores a ser analizado.')
    else:
        for valores in num:
            print(f' {valores}',end=' ')
            sleep(0.3)
        mai = max(num)
        quant = len(num)
        print(f'\nForam analisados {quant} valores e o maior valor entre eles é {mai} !')
        print('-='*30)

maior(11,8,15,10,12)
maior(25,23,25,24,26,29,27,20,9)
maior(1,23,4)
maior(0,23,25,1,2)
maior(0)
maior()