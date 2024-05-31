#Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.

lista = []
expressão = str(input('Digite sua expressão: '))

for símb in expressão:
    if símb == '(':
        lista.append('(')
    elif símb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0 :
    print('Sua expressão é valida.')
else:
    print('Sua expressão não é valida.')

#para cada vez que encontrar um par de parenteses ele ira remover,
#se a lista no final ficar vazia a expressão é valida,
# se sobrar algum parênteses é porque a expressão não é valida.