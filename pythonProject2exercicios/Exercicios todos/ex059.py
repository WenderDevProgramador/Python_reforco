#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = float('inf')
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            peso = maior
        if peso < menor:
            peso = menor
print('O maior peso lido foi {} KG.'.format(maior))
print('O menor peso lido foi {} KG.'.format(menor))
