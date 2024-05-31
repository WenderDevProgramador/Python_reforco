def aumentar(preço=0,taxa=0,formato=False):
    res = preço + (taxa * preço/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0,formato=False):
    res = preço - (taxa * preço/ 100)
    return res if formato is False else moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0,formato=False):
    res = preço/2
    return res if formato is False else moeda(res)

def moeda(preço=0, moeda= 'R$ '):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0,taxaa=0,taxar=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{moeda(preço)}')
    print(f'Dobro do valor: \t{dobro(preço,True)}')
    print(f'Metade do valor: \t{metade(preço,True)}')
    print(f'{taxaa}% de aumento:  \t{aumentar(preço,taxaa,True)}')
    print(f'{taxar}% de desconto: \t{diminuir(preço,taxar,True)}')
    print('-' * 30)

