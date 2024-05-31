'''PARA QUEM NÃO CONSEGUIU É SIMPLES

EXPLICAÇÃO: O float('inf', ele atribui um valor infinito positivo para a variável, logo qualquer peso menor que ele será verdadeiro na condição, ai basta realizarmos a atribuição do valor do peso sobre essa variável (nisso substituímos o valor infinito, para o da variável peso), e depois é só deixar a condição fazer o trabalho dela.

Obs: Eu falei que era simples, mas fiquei uma hora nesse exercício kkkk

CÓDIGO:
'''
maior_peso = 0
menor_peso = float('inf')

for c in range(1, 6):
    peso = float(input('Digite o seu peso: '))

    if peso > maior_peso:
        maior_peso = peso

    elif peso < menor_peso:
        menor_peso = peso

print('O maior peso lido foi de {:.1f}'.format(maior_peso))
print('O menor peso lido foi de {:.1f}'.format(menor_peso))
