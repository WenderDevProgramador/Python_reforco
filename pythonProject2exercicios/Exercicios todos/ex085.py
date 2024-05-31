#Exercício Python 080:
# Crie um programa
# onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for c in range(0,5):
    n = int(input(f'Digite {c+1}º número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O valor foi adicionado na última posição.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= len(lista):
                lista.insert(pos, n)
                print(f'O valor foi adicionado na {pos}ª')
                break
        pos += 1
print(f'A sequência da lista ficou {lista}')
