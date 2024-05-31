#Aprimorando o desafio 93:

#(Desafio 93)Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será quardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

print('  ')
print(f'{"==  Aproveitamento Time  ==":^60}')
print('  ')

jogadores = []
time = {}
gols = []

while True:
    gols.clear()
    time.clear()
    time["NOME:"] = str(input('Nome: ')).strip().upper()
    time["Nº DE PARTIDAS:"] = int(input('Quantas partidas jogou ? '))
    for g in range(0,time["Nº DE PARTIDAS:"]):
        gols.append(int(input(f'   Quantos gols {time["NOME:"]} marcou na {g+1}ª partida ?')))
    time["GOLS POR PARTIDA"] = gols[:]    
    time["Nº DE GOLS"] = sum(gols)
    jogadores.append(time.copy())
    
    novo = ' '
    while novo not in 'SN':
        novo = str(input('Deseja cadastrar outro jogador [S/N] ? ')).strip().upper()[0]
    if novo == 'N':
        break

print('='*60)
print(' ')
print(f'  {"== Dados do time ==":^60}  ')
print(' ')
print(f'{"Nº":<2} {"NOME":^12} {"Nº PARTIDAS":^14} {"Nº GOLS":^16}')
for i , d in enumerate(jogadores):
    print(f'{i:<2} {d["NOME:"]:^12} {d["Nº DE PARTIDAS:"]:^14} {d["Nº DE GOLS"]:^16}')
print('='*60)
print(' ')

while True:
    busca = int(input('Digite o número na tabela para ver mais dados induviduais[OU 999 ENCERRAR]: '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('Erro! Digite o número de acordo com a fixa do time.')
    else: 
        print(f'   == Levantamento Jogador {jogadores[busca]["NOME:"]}.')
        for g , d in enumerate(jogadores[busca]["GOLS POR PARTIDA"]):
            print(f'     == Na {g+1}ª partida marcou {d} gols !')
        print('-'*60)
    
print('Finalizando . . .')
print('  ')