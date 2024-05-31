#Exercício Python 089:
# Crie um programa que leia
# nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final,
# mostre um boletim contendo
# a média de cada um e permita que o usuário possa
# mostrar as notas de cada aluno individualmente.

lista = []

while True:
    n = str(input('NOME: ')).upper().strip()
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([n,[nota1, nota2],media])
    continua = ' '
    while continua not in 'SsNn':
        continua = str(input('Continua [S/N]: ')).strip()[0]
    if continua in 'Nn':
        break
print('-'*30)
print(f'{" BOLETIM ":-^30}')
print('-'*30)
print(f'{"Nº"} {" ALUNO ":^10} {" MÉDIA ":^18}')

for b , i in enumerate(lista):
    print(f'{b}  {i[0]:^10}   {i[2]:^12}')
ver = 0
while ver != 999:
    ver = int(input('Digite o número do aluno para ver as notas individuais ou [999] para finalizar: '))
    if ver <= len(lista):
        print(f'ALUNO: {lista[ver][0]}   NOTA: {lista[ver][1]}')
        print('-' * 30)
print('FINALIZANDO. . .')