#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será ou não mostrado o processo de cálculo do fatorial.

def fatorial(n,show=False):
    """_summary_
    --> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra o cálculo da conta.
    :return: O valor do Fatorial de um número n.
    """
    print('  ')
    f = 1
    print(f'{n}! = ',end='')
    for c in range(n,0,-1):
        f *= c
        if show:
            print(c,end=' ')
            if c > 1:
                print('X',end=' ')
            else:
                print('=',end=' ')
        
    print(f)
    return f
    print('  ')
  
fatorial(5,True)
help(fatorial)