'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opção = 0

while opção != 5:
    print('=-=-'*20)
    print('''Diga oque deseja fazer com os valores digitados:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')

    opção = int(input('Digite a opção acima: '))
    if opção == 1:
        print('O resultado de {} + {} = {}'.format(n1,n2,n1+n2))
    elif opção == 2:
        print('O resultado de {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('O valor maior entre {} e {} é {}'.format(n1, n2, maior))
        else:
            maior = n2
            print('O valor maior entre {} e {} é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Ok. Escolha novos valores')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    else:
        print('Opção invalida tente novamente.')
print('OK.Finalizando . . .')
