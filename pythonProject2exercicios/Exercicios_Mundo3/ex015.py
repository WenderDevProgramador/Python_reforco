##Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela com a formatação correta.
#a)A soma de todos os valores pares digitados.
#b)A soma dos valores da terceira coluna.
#c)O maior valor da segunda linha.
print('  ')
spar = mai = coluna = 0 
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número para {l}.{c}: '))
print('  ') 
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^8}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print(' ')
print('  ')
for l in range(0,3):
    if matriz[l][2]:
        coluna += matriz[l][2]

for c in range(0,3): 
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
               
print(f'O valor de todos os número pares digitados é {spar}.')
print(f'O valor da soma da terceira coluna é {coluna}.')
print(f'O maior valor da segunda linha é {mai}.')