from datetime import date
from time import sleep
ano=int(input('Digite o ano, para o ano atual digite apenas 0 :'))
if ano == 0:
    ano=date.today().year
print('Analisando o ano digitado...')
sleep(1)
if ano%4==0 and ano%100!=0 or ano%400==0: #nunca esquecer os : para dar continuidade no codigo
    print('O ano {} é BISSESTO!!'.format(ano))
else:
    print('O ano {} não é BISSESTO!'.format(ano))
#!= significa diferente
#time biblioteca  função sleep para dar delay nas respostas
#datetime biblicoteca de data função date trabalha com a data da maquina
