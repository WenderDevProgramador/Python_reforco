#Exercício Python 103:
# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<jogador desconhecido>',gols=0):
    print(f'O jogador {jog} fez {gols} gol(s).')


nome = str(input('Nome do jogador: ')).title()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)
