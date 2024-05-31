#Exercício Python 094:
# Crie um programa que leia nome,
# sexo e idade de várias pessoas,
# guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
from time import sleep
dici = {}
lis = []
tot = 0
while True:
    n = str(input('NOME: ')).strip().upper()
    while True:
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if s in 'MF':
            break
    i = int(input('Idade: '))
    tot += i
    while True:
        c = str(input('Continuar [S/N]? ')).strip().upper()[0]
        if c in 'SN':
            break
    dici['NOME'] = n
    dici['Sexo'] = s
    dici['Idade'] = i
    lis.append(dici.copy())
    if c == 'N':
        break
média = tot/len(lis)
print(f'A) Foram cadastradas no total de {len(lis)} pessoas.')
print(f'B) A média de idade das pessoas cadastradas é {média:5.2f} .')
print(f'C) O nome das mulheres cadastradas: ')
for p in lis:
    if p['Sexo'] == 'F':
        print(f'   ')
        for pessoa, dados in p.items():
            print(f'{pessoa} = {dados};',end=' ')
        sleep(1)
        print(' ')
print(f'\nD) As pessoas com idade acima da média são:')
for p in lis:
    if p['Idade'] > média:
        print(f'    ')
        for pessoa, dados in p.items():
            print(f'{pessoa} = {dados};',end=' ')
        sleep(1)
        print('  ')
print('-='*20)
print('  == ENCERRANDO ==   ')
