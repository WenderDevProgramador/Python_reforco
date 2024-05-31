#Exercício Python 67:
# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('==' * 20)
print('{:^40}'.format(' TABUADA '))
print('==' * 20)
while True:
    print('--' * 20)
    n = int(input('Digite um número para ver a tabuada: '))
    print('--' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
print('TABUADA ENCERRADA!')







