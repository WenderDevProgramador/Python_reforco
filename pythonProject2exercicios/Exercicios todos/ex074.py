#Exercício Python 69:
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.
cont18 = homens = mulher20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    if idade > 18:
        cont18 += 1
    while sexo not in 'FM':
        sexo = str(input('Qual é o sexo? [F/M]: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Pessoa cadastrada. Deseja continuar ? [S/N]: ')).upper().strip()[0]
    if continua == 'N':
        break
print(f'Da lista o total de pessoas com mais de 18 anos são {cont18} .')
print(f'Foram cadastrados o total de {homens} homens.')
print(f'E o total de {mulher20} mulher com menos de 20 anos.')
