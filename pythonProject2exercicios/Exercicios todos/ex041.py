#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário,
# 2 para octal e 3 para hexadecimal.
num=int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão:
[1]Converter para BINARIO.
[2]Converter para OCTAL.
[3]Converter para HEXADECIMAL.''')
opçao=int(input('Digite a opção selecionada acima: '))
if opçao==1:
    print('''O numero digitado foi {} á conversão para BINARIO é {}'''.format(num,bin(num)[2:]))
elif opçao==2:
    print('''O numero digitado foi {} á conversão para OCTAL é {}'''.format(num,oct(num)[2:]))
elif opçao==3 :
    print('''O numero digitado foi {} á conversão para HEXADECIMAL é {}'''.format(num,hex(num)[2:]))
else:
    print('Opção invalida tente novamente!')
