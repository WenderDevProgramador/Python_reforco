# Exercício Python 101:
# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(n=0):
    from datetime import date
    atual = date.today().year
    idade = atual - n
    if idade > 15 and idade < 18 or idade >= 70:
        return f'{idade} anos. VOTO OPCIONAL!'
    if idade >= 18 and idade < 70:
        return f'{idade} anos.VOTO OBRIGATORIO!'
    if idade < 16:
        return f'{idade} anos.VOTO NEGADO!'


print('-'*30)
idade = int(input('Em que ano você nasceu ? '))
voto(idade)