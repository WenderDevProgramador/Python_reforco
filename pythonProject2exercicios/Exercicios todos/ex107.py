#Exercício Python 102:
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    '''
    --> Calculo de fatorial de um número.
    :param n: Número a ser inserido para ver o fatorial
    :param show: (Opcional) Mostrar ou não a conta.
    :return: Valor do fatorial de n.
    '''

    f = 1
    for c in range(n,0,-1):
        if show:
            if c > 1:
                print(f'{c} X',end=' ')
            else:
                print(f'{c} = ',end=' ')
        f *= c
    return f



print(fatorial(5,True))
help(fatorial)