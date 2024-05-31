from random import randint
from time import sleep

n=int(randint(0,5))
print('Vou pensar em um numero tente adivinhar ...')
sleep(2)
print('-=-='*20)
sleep(2)
print('Pensando...')
sleep(2)
print('-=-='*20)
sleep(2)
q=int(input('Adivinhe o numero de 0 a 5: '))
print('Processando...')
sleep(3)
if q==n:
    print('Acertou miseravi !!!')
else:
    print('Perdeu kkkk tente de novo! O numero que pensei foi {}'.format(n))
