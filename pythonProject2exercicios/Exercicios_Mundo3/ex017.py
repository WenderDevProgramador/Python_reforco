#Crie um programa que leia o nome e duas notas de varios alunos e guarde tudo em uma lista composta. NO final, mostre um boletim contendo média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
print('  ')

boletim = []

while True:
    nome = str(input('NOME: ')).strip().upper()
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome,[nota1,nota2],media])
    continua = '  '
    while continua not in 'SN':
        continua = str(input('Cadastrar outro aluno ? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print('  ')
print('-'*40)
print(f'{"Nº":<2} {"NOME":^17} {"MÉDIA":^18}')    
print('-'*40)

for n, d in enumerate(boletim):
    print(f'{n:<2} {d[0]:^17} {d[2]:^18.2f}')
print('-'*40)    

while True:
    ver = int(input('Digite o número do aluno para ver a nota individual: '))
    if ver >= len(boletim):
        print('Número invalido digite de acordo com o boletim! ')
    else:
        print(f'O aluno {boletim[ver][0]} tem as seguintes notas {boletim[ver][1]}.')
        print('-'*40)
    outro = '  '
    while outro not in 'SN':    
        outro = str(input('Ver outro aluno? [S/N]: ')).strip().upper()[0]
    if outro == 'N':
        break
print('Obrigado!  FIM . . .')
print('  ')
