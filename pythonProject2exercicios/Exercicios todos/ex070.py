# Exercício Python 65:
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

núm = para = maior = cont = soma = 0
menor = 9999999999999
while para != 'N':
    núm = int(input('Digite um número: '))
    soma = soma + núm
    cont += 1
    para = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if núm == 1:
        maior = núm
        menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm

print('A média entre os valores digitados é {}.'.format(soma/cont))
print('O maior valor é {} e o menor é {}'.format(maior,menor))

