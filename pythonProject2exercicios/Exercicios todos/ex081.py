#Exercício Python 076:
# Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos preços, na sequência.
# No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.
print('-='*19)
print(f' {"LISTAGEM DE PREÇO":^35} ')
print('-='*19)
listagem = ('Lapis',1,
            'Caneta',2,
            'Borracha',0.50,
            'Apontador',1.50,
            'Lapiseira',3.50,
            'Chames',9.99,
            'Cartolina',2.50,
            'Caderno',12.90,
            'Agenda',15.30,
            'Estojo',16,
            'Mochila',120.89)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-='*19)
