from math import hypot
co=float(input('Qual o comprimento do cateto oposto ? '))
ca=float(input('Qual o comprimento do cateto adjacente ? '))
hi=hypot(co,ca)
print('O comprimento da Hipotenusa é {:.2f} '.format(hi))

#tudo que envolver matematica procura a função que calcule na biblioteca math

'''co=float(input('Qual é o comprimento do cateto oposto ? '))
ca=float(input('Qual é o comprimento do cateto adjacente ? '))
hi=(co**2+ca**2)**(1/2)
print('O comprimento da Hipotenusa é {:.2f} '.format(hi))'''



