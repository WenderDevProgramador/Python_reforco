#Exercício Python 70:
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

print('~~'*20)
print('~~'*20)
print('_-'*20)
print('{:^40}'.format(' LOJAS BARATÃO '))
print('_-'*20)
print('~~'*20)
print('~~'*20)
totcomp = contmil =  cont = 0
nmenor = ' '
menor = 99999999999999999

while True:
    produto = str(input('Qual o produto deseja resgistrar? ')).upper().strip()
    valor = float(input('Qual o valor do produto? R$ '))
    cont += 1
    totcomp += valor
    if valor == 1 or valor < menor:
        menor = valor
        nmenor = produto
    if valor > 1000:
        contmil += 1
    prociga = ' '
    while prociga not in 'SN':
        prociga = str(input('Deseja registrar mais ? [S/N]: ')).upper().strip()[0]
    if prociga == 'N':
        break
print('{:-^60}'.format(' RESUMO DA COMPRA '))
print(f'O valor total da compra foi R${totcomp:.2f}.')
print(f'No total de {contmil} produto custo mais de R$1000,00 reais.')
print(f'O produto de menor valor é {nmenor} e o seu preço é R${menor:.2f}')