#Desenvolva um programa que leia quatro valores e os guarde em uma tupla. 
#E no final mostre:
#a) Quantas vezes apareceu o valor 9.
#b) Em que posição foi digitado o valor 3.
#c) Quais foram os números pares.
print('  ')
num = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))

print('  ')

print(f'O número 9 apareceu {num.count(9)} vez.')

if 3 in num: 
    print(f'O valor 3 foi digitado na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não aparece na lista.')
    
print(f'Os números pares digitados foram:',end=' ')

for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
        