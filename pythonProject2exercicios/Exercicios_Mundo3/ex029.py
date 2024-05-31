#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.

def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        print(f'Sua idade é {idade} anos!')
        print(f'VOTO NEGADO!')
    elif idade >= 16 and idade < 18 or idade >= 70:
        print(f'Sua idade é {idade} anos!')
        print('VOTO FACULTATIVO')
    else:
        print(f'Sua idade é {idade} anos!')
        print('VOTO OBRIGATORIO!')
    



print('  ')
ano =  int(input('Qual o ano de nascimento? '))
voto(ano)
print('  ')
