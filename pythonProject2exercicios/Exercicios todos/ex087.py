#Exercício Python 082:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista1 = []
listaimpar = []
listapar = []

while True:
    n = int(input('Digite um valor para adicionar: '))
    lista1.append(n)
    if n % 2 == 1:
        listaimpar.append(n)
    if n % 2 == 0:
        listapar.append(n)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar ? [S/N] ' )).strip().upper()[0]
    if continua in 'N':
        break
print(f'A lista principal ficou assim {lista1} .')
print(f'A lista com os números impares ficou assim {listaimpar}. ')
print(f'A lista com os números pares ficou assim {listapar} .')