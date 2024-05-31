#Exercício Python 085:
# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final,
# mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]

for c in range(1,8):
    n = int(input(f'Digite o número para cadastrar {c}º: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
print(lista)
print(f'Os números pares são: {lista[0]}')
print(f'Os números impares são: {lista[1]}')