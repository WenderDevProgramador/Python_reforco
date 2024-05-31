'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
#PARA SE FORMA UM TRIÂNGULO O SEGUIMENTO MAIOR NÃO PODE SER MAIOR QUE A SOMA DOS OUTROS DOIS.
print('-=-='*20)
print('-=-='*20)
print('\033[1;31m Analisador de triângulos\033[m')
print('-=-='*20)
print('-=-='*20)
n1=float(input('Digite o valor do primeiro seguimento: '))
n2=float(input('Digite o valor do segundo seguimento: '))
n3=float(input('Digite o valor do terceiro seguimento: '))
print('Os valores são {}, {} e {}.'.format(n1,n2,n3))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Podem formar TRIÂNGULO!')
    if n1 == n2 == n3:
     print('TRIÂNGULO EQUILÁTERO!')
    elif n1 != n2 != n3 != n1 :
        print('TRIÂNGULO ESCALENO!')
    else:
        print('TRIÂNGULO ISÓSCELES')
else:
    print('Não podem formar um TRIÂNGULO!')

