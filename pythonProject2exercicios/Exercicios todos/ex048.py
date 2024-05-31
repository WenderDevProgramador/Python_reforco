'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAS QUEIROZ '))

preço=float(input('Qual o valor do produto ? R$ '))
condiçao=int(input('''\033[1;34m Para escolher a forma de pagamento. 
 Digite a opção a baixo\033[m : 
–[1] à vista dinheiro/cheque: 10% de desconto

–[2] à vista no cartão: 5% de desconto

–[3] em até 2x no cartão: preço formal 

–[4] 3x ou mais no cartão: 20% de juros:  '''))
print('\033[1;31m Analisando o pagamento . . .\033[m')
if condiçao == 1:
    print('O valor a ser pago é R$ {:.2f}'.format(preço - (10*preço/100)))
elif condiçao == 2 :
    print('O valor a ser pago é R$ {:.2f}'.format(preço - (5*preço/100)))
elif condiçao == 3 :
    print('O valor a ser pago é R$ {:.2f}'.format(preço))
elif condiçao == 4 :
    print('O valor a ser pago é R$ {:.2f}'.format(preço + (20*preço/100)))
else:
    print('Você escolheu a opção invalida!')
