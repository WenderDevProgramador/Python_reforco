#Exercício Python 079:
# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    n = int(input('Digite um valor para adicionar:'))
    if n not in lista:
        lista.append(n)
        print('Valor registrado!!')
    else:
        print('Valor repetido, não vou adicionar.')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continua in 'N':
        break
lista.sort()
print(f'{lista}')
