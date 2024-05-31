#Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
#Número primo é um número que é divisivel apenas duas vezes, por 1 e ele mesmo.
núm=int(input('Digite um número: '))
tot=0
for c in range(1,núm+1):
    if núm % c ==0:
        print('\033[1;31m {}'.format(c),end=' ')
        tot=tot+1
    else:
        print('\033[m {}'.format(c),end=' ')
print('\nO número {} foi divisivél {} vez'.format(núm,tot))
if tot == 2 :
    print('\033[34mÉ um número primo pois só foi divisivél por 1 e ele mesmo!')
else:
    print('\033[33mNão é um número primo!')
    