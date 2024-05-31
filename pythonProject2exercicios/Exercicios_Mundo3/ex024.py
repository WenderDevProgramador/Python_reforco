#Faça um programa que tenha uma função chamada área(), que recebe as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
print(' ')
def área(larg,compri):
    a = larg * compri
    print(f'A área de um terreno {larg} X {compri} é {a}m².')

    
print('  == Controle de terrenos')
print('-'*30)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l,c)