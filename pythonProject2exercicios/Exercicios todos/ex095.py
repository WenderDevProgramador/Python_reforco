#Exercício Python 090:
# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final,
# mostre o conteúdo da estrutura na tela.
dicionario = {}
nome = str(input('Nome aluno: '))
media = float(input('Media aluno: '))
dicionario['Nome'] = nome
dicionario['Media'] = media
if media >= 7 :
    dicionario['Situação'] = 'Aprovado'
elif media >= 5 and media < 7:
    dicionario['Situação:'] = 'Recuperação'
else:
    dicionario['Situação:'] = 'Reprovado'
for k, v in dicionario.items():
    print(f'{k} é {v}')