#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrecente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

ano_atual = datetime.date.today().year

dicionario = {}

print('   == Cadastro de pessoas ==   ')
print('   ')

dicionario["NOME"] = str(input('NOME: ')).strip().upper()
dicionario["ANO DE NASCIMENTO"] = int(input('ANO DE NASCIMENTO: '))
dicionario["CTPS"] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM): '))
dicionario["IDADE"] = ano_atual - dicionario["ANO DE NASCIMENTO"]

if dicionario["CTPS"] > 0:
    dicionario["ANO DE CONTRATAÇÃO"] = int(input('ANO DE CONTRATAÇÃO: '))
    dicionario["SALARIO"] = float(input('SALÁRIO: R$ '))
    dicionario["IDADE DE APOSENTAR"] = (dicionario["ANO DE CONTRATAÇÃO"] + 45 ) - dicionario["ANO DE NASCIMENTO"] 

print('-='*20)

for k, d in dicionario.items():
    print(f'  - {k} = {d}')
    

