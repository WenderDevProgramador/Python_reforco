#Exercício Python 114:
#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from time import sleep
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.mercadolivre.com/'),sleep(2)

except(KeyboardInterrupt):
    print('ERRO! Usuario interrompeu o processo')


except:
    print('ERRO! Não conseguimos acessar a pagina!')


else:
    print('Pagina acessada com sucesso.')