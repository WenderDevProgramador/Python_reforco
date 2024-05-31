#Exercício Python 66:
# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = soma = 0
while True:
    núm = int(input('Digite um número [999 para finalizar]: '))
    if núm == 999:
        break
    soma = soma + núm
    cont += 1
print(f'Você digitou {cont} números.')
print(f'A soma entre os números digitados é {soma}.')
