#Rescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.

from ultilidades import dados

print(' ')

v = dados.leiaInt('Digite um número inteiro: ')
print(f'O número digitado foi {v}')

i = dados.leiaFloat('Digite um número real: ')
print(f'O número digitado foi {i}')

print(' ')


