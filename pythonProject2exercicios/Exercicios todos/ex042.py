#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
from time import sleep
n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
print('\033[1;31m Comparando os numeros digitados . . .\033[m')
sleep(1)
if n1>n2:
    print('\033[1;34m O primeiro valor é maior!\033[m')
elif n1<n2:
    print('\033[1;34m O segundo valor é maior!\033[m')
elif n1==n2:
    print('\033[1;34m Não existe valor maior, os dois são iguais!\033[m')

