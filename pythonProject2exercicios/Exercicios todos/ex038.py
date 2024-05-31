s=float(input('Digite o seu salario atual : R$ '))
d=(s*10)/100+s
q=(s*15)/100+s
if s>1250:
    print('O seu salario é {:.2f} e com o aumento de 10% passa a ser R${:.2f}'.format(s,d))
else:
    print('O seu salario é {:.2f} e com aumento de 15% passa a ser R${:.2f}'.format(s,q))
