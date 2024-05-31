#A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

'''– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
from datetime import date
ano=int(input('Digite o ano em que você nasceu: '))
idade=date.today().year - ano
print('Sua idade é {}'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 14 >= idade > 9:
    print('Sua categoria é INFANTIL')
elif 19 >= idade > 14 :
    print('Sua categoria é JUNIOR.')
elif 25>= idade > 19 :
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
