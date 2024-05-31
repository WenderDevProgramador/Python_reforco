from random import shuffle
n1=str(input('Primeiro nome : '))
n2=str(input('Segundo nome : '))
n3=str(input('Terceiro nome : '))
n4=str(input('Quarto numero : '))
lista=[n1,n2,n3,n4]
r=shuffle(lista)
print('A ordem para apagar o quadro é {}'.format(lista))
