#Exercício Python 63:
#Escreva um programa que leia um número N inteiro qualquer
#e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8 = sempre soma os dois anteriores.
print('='*50)
print('-'*50)
print('{:^50}'.format('Sequência de Fibonacci'))
print('-'*50)
print('='*50)
n = int(input('Quantos termos da sequência de Fibonacci deseja vizualizar ?'))
t1 = 0
t2 = 1
print('{} --> {} -->'.format(t1,t2),end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{} -->'.format(t3),end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')