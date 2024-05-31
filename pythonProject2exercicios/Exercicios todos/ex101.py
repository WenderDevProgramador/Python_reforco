#Exercício Python 096:
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(l,c):
    r = l * c
    print(f'A aréa de um terreno  {l} x {c}  é de  {r:.2f}m².')


print('-='*30)
print(f'{"DIMENSÕES DE UM TERRENO":=^60}')
print('-='*30)
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
area(largura, comprimento)
