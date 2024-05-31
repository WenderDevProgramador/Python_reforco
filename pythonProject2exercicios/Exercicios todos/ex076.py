#Exercício Python 071:
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from time import sleep

print('-='*40)
print('{:=^80}'.format(' BANCO WSA '))
print('-='*40)
print('No momento esse caixa possui cédulas de R$50, R$20, R$10 e R$1')

valor = int(input('Qual será o valor do saque? R$ '))
print('Contando as cédulas . . .')
sleep(2)
print('Após a contagem retire o seu dinheiro no local indicado . . .')
sleep(2)
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1

    else:
        if totalced > 0:
            print(f'{totalced} cédulas de R${ced} foram entregues.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0

        if total == 0:
            break

print('-='*40)
print(f'Obrigado volte sempre!!')