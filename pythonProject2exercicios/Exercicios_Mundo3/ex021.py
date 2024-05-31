#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será quardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
print('   ')

jogador = {}
gols = []
gols.clear()

jogador['Nome Jogador'] = str(input('Nome Jogador: ')).strip().upper()
jogador['Partidas jogadas'] = int(input(f'Nº Partidas {jogador["Nome Jogador"]}: '))

for p in range(0,jogador[f'Partidas jogadas']):
    gols.append(int(input(f'   == > Quantas gols na {p+1}ª partida?  ')))

jogador['Gols Por Partida'] = gols[:]

print('-='*40)   
print(jogador)
print('-='*40)

print(f'Nome jogador: {jogador["Nome Jogador"]}')
print(f'Gos por partida feito {jogador["Gols Por Partida"]}')
print(f'O total de de gols foi {sum(gols)}')
print('-='*40)

print(f'O jogador {jogador["Nome Jogador"]} jogou {jogador["Partidas jogadas"]} partidas.')
for p, d in enumerate(gols):
    print(f'   == > Na partida {p+1}, fez {d} gols.')
print(f'O total de de gols foi {sum(gols)}')

print('   ')

