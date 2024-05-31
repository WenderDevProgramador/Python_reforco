#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.No final, mostre uma listagem de preço, organizando os dados em forma tabular.

compras = ('Caderno',2.75,'Mochila',99.99,'Lapís',1.50,'Lapizeira',5.00,'Borracha',2.00,'Lancheira',25.00,'Fichario',35.50) 

print('   ')
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)

for pos in range(0,len(compras)):
    if pos % 2 == 0:
        print(f'{compras[pos]:.<30}',end='')
    else:
        print(f'R${compras[pos]:>7.2f}')
print('-'*40)        