#Exercício Python 087:
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

tpares = tcoluna = maior = 0

for p in range(0,3):
    for l in range(0,3):
        matriz[p][l] = int(input(f'Digite para adiconar em {p} e {l}: '))
for p in range(0,3):
    for l in range(0,3):
        print(f'{matriz[p][l]:^5}',end=' ')
        if matriz[p][l] % 2 == 0:
            tpares += matriz[p][l]
    print()
print(f'A soma de todos os valores é {tpares} .')
for l in range(0,3):
    tcoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {tcoluna} .')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior} .')
