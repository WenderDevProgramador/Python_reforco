#Exercício Python 092:
# Crie um programa que leia nome,
# ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.

'''O homem ainda precisa ter no mínimo 35 anos de contribuição e a mulher no mínimo 30 anos de contribuição.'''
from datetime import date

data_atual = date.today().year
funcionarios = {}

funcionarios['NOME'] = str(input('NOME COLABORADOR: ')).upper().strip()
nasc = int(input('Ano de nascimento: '))
funcionarios['CARTEIRA'] = int(input('Número da carteira ou [0 se não tiver]: '))
funcionarios['IDADE'] = date.today().year - nasc

if funcionarios['CARTEIRA'] != 0:
    funcionarios['ANO DE CONTRATAÇÃO'] = int(input('Ano de contratação: '))
    funcionarios['SALARIO'] = float(input('Salario atual: '))
    sexo = int(input('Qual o sexo [1.Masc 2.Femi]: '))
    if sexo == 1:
        funcionarios['IADADE QUE APOSENTA'] = funcionarios['IDADE'] + ((funcionarios['ANO DE CONTRATAÇÃO']+35)- data_atual)
    elif sexo == 2:
        funcionarios['IADADE QUE APOSENTA'] = funcionarios['IDADE'] + ((funcionarios['ANO DE CONTRATAÇÃO']+30)- data_atual)
    else:
        print('Opção invalida digite 1 ou 2.')
        sexo = int(input('Qual o sexo [1.Masc 2.Femi]: '))
print('-='*20)
print(' == CADASTRO DO COLABORADOR == ')
for f, v in funcionarios.items():
    print(f'    {f} : {v} ')




