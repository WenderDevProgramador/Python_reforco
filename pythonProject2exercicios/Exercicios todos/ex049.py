#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens=('PEDRA','TESOURA','PAPEL')
maquina=randint(0,2)

print('\033[1;31m=\033[m'*60)
print('\033[1;31m{:=^70}'.format('  \033[mJokenpo\033[1;31m  '))
print('\033[1;31m=\033[m'*60)
jogador=(int(input('''PARA JOGAR SELECIONE A OPÇÃO ABAIXO:
[0] PARA PEDRA
[1] PARA TESOURA
[2] PARA PAPEL
''')))
from time import sleep
sleep(1)
print('\033[1;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO. . . \033[m')
sleep(1)

if maquina == jogador:
    print('EMPATAMOS VAMOS JOGAR NOVAMENTE!!')
    print('Maquina escolheu {}'.format(itens[maquina]))
    print('Você escolheu {}'.format(itens[jogador]))
elif maquina == 0 and jogador == 1 :
    print('VOCÊ PERDEU!!')
    print('Maquina escolheu {}'.format(itens[maquina]))
    print('Você escolheu {}'.format(itens[jogador]))
elif maquina == 1 and jogador == 2 :
    print('VOCÊ PERDEU!!')
    print('Maquina escolheu {}'.format(itens[maquina]))
    print('Você escolheu {}'.format(itens[jogador]))
elif maquina == 2 and jogador == 0 :
    print('VOCÊ PERDEU!!')
    print('Maquina escolheu {}'.format(itens[maquina]))
    print('Você escolheu {}'.format(itens[jogador]))
elif jogador == 0 and maquina == 1 :
    print('VOCÊ GANHOU!!')
    print('Maquina escolheu {}'.format(itens[maquina]))
    print('Você escolheu {}'.format(itens[jogador]))
elif jogador == 1 and maquina == 2 :
    print('VOCÊ GANHOU!!')
    print('Maquina escolheu {}'.format(itens[maquina]))
    print('Você escolheu {}'.format(itens[jogador]))
elif jogador == 2 and maquina == 0 :
    print('VOCÊ GANHOU!!')
    print('Maquina escolheu {}'.format(itens[maquina]))
    print('Você escolheu {}'.format(itens[jogador]))
else:
    print('OPÇÃO INVALIDA! JOGUE NOVAMENTE!')

