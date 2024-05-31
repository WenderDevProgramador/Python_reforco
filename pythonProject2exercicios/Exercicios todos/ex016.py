dias=int(input('Quantos dias o carro ficou alugado ?  '))
km=float(input('Quantos KM o carro percorreu no periodo alugado ? '))
preço=(dias*60)+(km*0.15)
print('O valor a pagar pelo aluguel é R${:.2f}'.format(preço))
