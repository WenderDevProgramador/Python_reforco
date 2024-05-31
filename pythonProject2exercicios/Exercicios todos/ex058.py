from datetime import date
'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
atual=date.today().year
maior=0
menor=0
for pessoas in range(1,8):
    nas=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade= atual - nas
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Da lista {} pessoas já atingiram a maioridade!'.format(maior))
print('Da lista {} pessoas ainda não atingiram a maioridade!'.format(menor))
