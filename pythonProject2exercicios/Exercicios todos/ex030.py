n = str(input('Qual é o seu nome ?')).strip().title()
nome = n.split()
print('Muito prazer em te conhecer...')
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1]))
#split é lista logo se trabalha com [] função len vai contar
#os elementos dentro da lista começando
# por 0 dessa forma se coloca o menos 1 para descobri a ultima palavra.
