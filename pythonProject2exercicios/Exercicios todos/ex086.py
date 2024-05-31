#Exercício Python 081:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = int(input('Digite um valor para ser adicionado a lista : '))
    lista.append(n)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar a adicionar [S/N]? ')).strip().upper()[0]
    if continua in 'N':
        break
print(f'Na lista temos {len(lista)} elementos. ')
lista.sort(reverse=True)
print(f'{lista} .')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')