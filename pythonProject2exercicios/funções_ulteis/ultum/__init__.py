
def moeda(preço=0,papel='R$'):
    res = f'R$ {preço:.2f}'
    return res

def aumentar(preço=0,taxa=0,formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0,taxa=0,formato=False):
     res = preço - (preço * taxa/100)
     return res if formato is False else moeda(res)
 
def dobro(preço=0,formato=False):
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0,formato=False):
    res = preço / 2
    return res if not formato else moeda(res)  

def resumo(valor,au=5,me=3):
    preço =  moeda(valor)
    aumento = aumentar(valor,au,True)
    diminui = diminuir(valor,me,True)
    dobrar = dobro(valor,True)
    corta = metade(valor,True)
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'Preço analisado:  \t{preço:>4}')
    print(f'Dobro do preço:   \t{dobrar:>4}')
    print(f'Metade do preço:  \t{corta:>4}')
    print(f'{au}% de aumento:   \t{aumento:>4}')
    print(f'{me}% de redução:   \t{diminui:>4}')
    print('-'*35)

'''
is (É)
or (OU)
and (TAMBÉM)
'''