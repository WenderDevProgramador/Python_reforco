from time import sleep
'''Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.'''
casa=float(input('Digite o valor da casa a ser financiada:R$ '))
tempo=int(input('Digite em quantos anos pretende pagar o financiamento: '))
salario=float(input('Digite o valor da sua renda mensal:R$ '))
fin=casa/(tempo*12)
renda=fin/salario*100
print('\033[1;31m Fazendo a sua simulação \033[m. . .')
sleep(2)
print('O valor da parcela fica R${:.2f}'.format(fin))
print('\033[1;34m Analisando aprovação do financiamento . . .\033[m')
sleep(2)
if renda <=30:
    print('\033[1;34m Seu financiamento foi aprovado!\033[m')
else:
    print('''\033[1;31m Infelizmente não podemos aprovar o seu financiamento no memento!
    Pois o valor da prestação não pode ultrapassar 30% do valor da sua renda.
    E a sua parcela ficou em {:.0f}% do valor da sua renda'''.format(renda))

