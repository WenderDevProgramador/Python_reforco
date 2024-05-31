#Exercício Python 075:
# Desenvolva um programa que
# leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

núm =  (int(input(f'Digite o 1º número: ')),
       int(input(f'Digite o 2º número: ')),
       int(input(f'Digite o 3º número: ')),
       int(input(f'Digite o 4º número: ')))
print(f'Os valores digitados são {núm}')
print(f'O número 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
       print(f'O valor 3 foi digitado na {núm.index(3)+1}ª posição.')
else:
       print('O valor 3 não apareceu na sequencia digitada.')
print(f'Os números pares são ',end=' ')
for c in núm:
       if c % 2 == 0 and c != 0:
              print(c,end='  ')







