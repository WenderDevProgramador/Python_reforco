#Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

print('{}'.format(" === DESEMPENHO DO ATLETA === "))
jogador = {}
golsfeitos = []
jogador['NOME JOGADOR'] = str(input('Nome jogador: ')).upper().strip()
jogador['Nº PARTIDAS'] = int(input(f'Nº de partidas de {jogador["NOME JOGADOR"]}: '))

for g in range(0,jogador['Nº PARTIDAS']):
    golsfeitos.append(int(input(f'Quantos gols foram marcados por {jogador["NOME JOGADOR"]} na {g+1}ª partida? ')))

jogador['Nº DE GOLS FEITO'] = sum(golsfeitos)
jogador['Nº GOLS PARTIDA'] = golsfeitos[:]
print('-='*20)
print(jogador)
print('-='*20)
for j,d in jogador.items():
    print(f'    ==> {j} --- {d} .')
print('-='*20)
print(f'O {jogador["NOME JOGADOR"]} jogou o total de {jogador["Nº PARTIDAS"]} partidas.')
print(f'{jogador["NOME JOGADOR"]} fez um total de {jogador["Nº DE GOLS FEITO"]} gols.')
for p, g in enumerate(golsfeitos):
    print(f'Na {p+1}ª partida fez {g} gols.')
