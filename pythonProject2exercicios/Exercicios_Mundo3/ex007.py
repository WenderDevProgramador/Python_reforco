#Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista.
print(' ')

lista = []
mai = 0
men = 99999999999999999999
for v in range(0,5):
    lista.append(int(input(f'Digite um valor para {v+1}ª  posição: ')))
    if v == 0:
        mai = men = lista[v]
    else:
        if lista[v] > mai:
            mai = lista[v]
        if lista[v] < men:
            men = lista[v]
print(' ')
print(lista)
print(' ')
print(f'O maior valor digitado foi {mai} e o menor valor digitado foi {men}.')
print(f'O número {mai} está nas seguintem posições, ',end='')
for n, v in enumerate(lista):
    if v == mai:
        print(f'{n+1}',end='...')
print(' ')    
print(f'\nO número {men} está nas seguintem posições, ',end='')
for n, v in enumerate(lista):
    if v == men:
        print(f'{n+1}',end='...')
print(' ')
