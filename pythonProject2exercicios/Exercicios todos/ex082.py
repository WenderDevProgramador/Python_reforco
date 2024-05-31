#Exercício Python 077:
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('banana','feijao','arroz','progrmador','python','java',
            'php','pumba','simba','garoto','chocolate','nestle','tapioca','queijo')

for ordem in palavras:
    print(f'\nNa palavra {ordem.upper()} temos as seguintes vogais',end='  ')
    for letra in ordem:
        if letra.upper() in 'AEIOU':
            print(letra.upper(),end='  ')