#Exercício Python 64:
#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final,
#mostre quantos números foram digitados e
#qual foi a soma entre eles (desconsiderando o flag).
n = cont = soma = 0
n = int(input('Digite um número ou digite [999 para finalizar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número ou digite [999 para finalizar]: '))
print('O valor total dos números digitados é {}'.format(soma))
print('Foram digitados {} números.'.format(cont))
