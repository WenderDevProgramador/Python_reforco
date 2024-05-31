# Melhore o jogo do DESAFIO 28
# onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('==='*20)
print('{:^60}'.format(' JOGO DE ADIVINHAÇÃO '))
print('==='*20)
número = int(input('Tente adivinhar o número de 0 a 10. Digite o número:'))
palpites = 0
n=randint(0,10)

while número != n:
    if número > 10:
        print('Opção invalida você só pode escolher entre 0 e 10')
    if número > n:
        print('Menos...')
    else:
        print('Mais...')
    print('O número escolido pela maquina foi {}, e você escolheu  {} !'.format(n, número))
    número = int(input('Você perdeu !! Tente novamente : '))
    palpites = palpites + 1
print('O número escolido pela maquina foi {}, e você escolheu  {} !'.format(n,número))
print('Parabéns você ganhou !!', end=' ')
print('Você precisou de {} chances para acerta !'.format(palpites + 1))


#Como o meu ficou diferente deixei essa explicação para fazer igual o Gustavo na correção dele.
'''Esses valor boleano not foi bem pouco falado. 
Então vou deixar como eu entendi a lógico do Guanabara. 

acertou = True
O valor lógico boleano not investe os valores. 
No código acima, acertou recebe False*, 
na estrutura de repetição, o *not está invertendo o valor False para True*, 
fazendo o loop continua (lembra do que o *while só sai do loop se dá False*)  
depois ele coloca uma condição no loop para substituir *acertou para True e  
consequentemente o not investe para False , saindo do loop.'''