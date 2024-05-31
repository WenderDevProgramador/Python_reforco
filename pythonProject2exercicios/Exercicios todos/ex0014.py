salario=float(input('Qual é o seu salario ? R$ '))
novo=salario + (salario*15/100)
print('Seu salario atual é R$ {:.2f} e com o aumento de 15% seu novo salario sera R$ {:.2f}'.format(salario,novo))