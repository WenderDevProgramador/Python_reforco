#Crie um programa aonde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
#e fechados na ordem correta.
print('  ')
pilha = []

expre = str(input('Digite sua expresão para validar:  '))

for v in expre:
    if v == '(':
        pilha.append('(')
    if v ==')':
        if len(pilha) == 0:
            pilha.append(')')
        else:
            pilha.pop()

if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão não está correta!')
print('  ')