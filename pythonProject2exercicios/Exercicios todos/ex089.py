#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
lista = []
temporaria = []
maior = 0
menor = 99999999999999999999
while True:
    temporaria.append(str(input('Nome: ')).upper().strip())
    temporaria.append(int(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    lista.append(temporaria[:])
    temporaria.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Continua a cadastrar ? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break

print(f'O total de pessoas cadastradas foi {len(lista)}')
print(f'O maior peso é {maior} . E são de , ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')

print(f'\nO menor peso é {menor} .E são de ,', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')




