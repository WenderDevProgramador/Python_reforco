#Exercício Python 72:
# Crie um programa
# que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

vari = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze',
        'dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número para ler por extenso [entre 0 e 20]:'))
    while num > 20:
        print('Opção invalida!')
        num = int(input('Digite um número para ler por extenso [entre 0 e 20]:'))
    while num < 0:
        print('Opção invalida!')
        num = int(input('Digite um número para ler por extenso [entre 0 e 20]:'))
    print(f'{vari[num]}')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar a ver ?[S/N] ')).upper().strip()[0]
    if continua == 'N':
        break

print('FIM')