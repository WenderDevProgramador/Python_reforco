# Exercício Python 095:
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
golsmarcados = []
jogador = {}
time = []
print('-=' * 30)
print('     === INSERINDO OS DADOS PARA ANALISE DO ATLETA ===     ')
print('-=' * 30)
while True:
    golsmarcados.clear()
    jogador.clear()
    jogador['NOME'] = str(input('Nome jogador: ')).upper().strip()
    jogador['PARTIDAS JOGADAS'] = int(input('Quantas partidas jogadas: '))
    for j in range(0, jogador['PARTIDAS JOGADAS']):
        golsmarcados.append(int(input(f'Quantos gols {jogador["NOME"]} fez na partida {j + 1} ?')))
    jogador['TOTAL GOLS'] = sum(golsmarcados)
    jogador['GOLS POR PARTIDA'] = golsmarcados[:]
    time.append(jogador.copy())
    while True:
        c = str(input('Cadastrar outro jogador [S/N]? ')).upper().strip()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
        
print('-=' * 30)
print(f'{" DADOS DO TIME ":=^60}')
print('-=' * 30)
print(f'{"Nº"}{"NOME":-^14}{"Nº DE PARTIDAS":-^26}{"TOTAL DE GOLS":->20}')
print('--' * 30)
for j, d in enumerate(time):
    print(f'{j} = {d["NOME"]:^10} {d["PARTIDAS JOGADAS"]:^24} {d["TOTAL GOLS"]:^30}')
print('--' * 30)
while True:
    dados_jogador = int(input('Digite o número do jogador ou [999] para finalizar: '))
    if dados_jogador == 999:
        break
    if dados_jogador > len(time):
        print('ERRO...')
        print('Esse número de jogador não existe veja de acordo com os dados do time.')
    else:
        print(f'---->> Segue dados de gols por partida do jogador {time[dados_jogador]["NOME"]}!!')
        for j, d in enumerate(time[dados_jogador]["GOLS POR PARTIDA"]):
            print(f'    ==> Na partida {j+1} , {time[dados_jogador]["NOME"]} marcou {d} gols !!')

print('== Finalizando ==')
