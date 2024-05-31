#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# o termo e o número que começa e a razão o número que ira pular
print('Gerador de uma PA')
print('=='*10)
primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -->'.format(termo),end=' ')
    termo = termo + razao
    cont = cont + 1
print('FIM')