#Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
maioridade = 0
maisvelho = ''
totmulher20 = 0
for i in range(1,5):
    print(('='*10),' {}ªPESSOA '.format(i),('='*10))
    nome = str(input('Digite o seu nome: ')).strip().upper()
    idade=int(input('Digite a sua idade: '))
    sexo=str(input('Digite o seu sexo [M/F]: '))
    somaidade= somaidade + idade
    if i == 1 and sexo in 'Mm':
        maioridade = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
print('Ao todo na lista temos o {} total de mulheres com menos de 20 anos.'.format(totmulher20))
print('O homem mais velho é {} e ele tem {} anos.'.format(maisvelho,maioridade))
print('A média de idade do grupo é: {}'.format(somaidade/4))
