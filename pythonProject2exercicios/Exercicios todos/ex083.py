#Exercício Python 078:
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for c in range(1,6):
    lista.append(int(input(f'Digite o valor da {c}ª posição: ')))
print(f'Os valores adicionados a lista foi {lista} .')
print(f'O maior valor da lista é {max(lista)} . E está na posição ',end='')
for p , v in enumerate(lista):
    if v == max(lista):
        print(f'{p+1}...', end='')
print(f'\nO menor valor da lista é {min(lista)} .E está na posição ', end='')
for p , v in enumerate(lista):
    if v == min(lista):
        print(f'{p+1}...', end='')
