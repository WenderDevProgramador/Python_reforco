#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso,você deverá mostrar para cada palavra,
#quais são suas vogais.
print('   ')
print('-'*30)
print(f'{"PALAVRAS E SUAS VOGAIS":^30}')
print('-'*30)

palavras = ('Crie', 'um', 'programa', 'que', 'tenha', 'uma', 'tupla' ,'com','palavras')

print('   ')

for p in palavras:
    print(f'\nNa palavra "{p.upper()}" temos as seguintes vogais, ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
            
print('   ')
            