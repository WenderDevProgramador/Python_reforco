#Crie um programa aonde o usúario possa
#digitar 7 valores númericos e cadastreos
#em uma lista única que mantenha separado 
#os valores pares e valores impares.
#No final mostre os valores pares e impares em ordem crescente.
print("  ")
lista = [[],[]]

for n in range(0,7):
    num = int(input(f'Digite o {n+1}º valor para adicionar: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os números cadastrados foram {lista}.')
print(f'Os números pares cadastrados foram {lista[0]}.')
print(f'Os números impares cadastrados foram {lista[1]}.')
