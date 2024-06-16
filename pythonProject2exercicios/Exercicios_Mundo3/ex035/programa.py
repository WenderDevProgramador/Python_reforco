#Adapte o código do exercício anterior , criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.


import funções

print()

preço = float(input('Digite um preço R$: '))

print(f'O preço {funções.moeda(preço)} com um aumento para compra a prazo  fica {funções.aumentar(preço,5)}')
print(f'O preço {funções.moeda(preço)} com um desconto  para pagamento avista fica {funções.diminuir(preço,5)}')
print(f'O dobro de {funções.moeda(preço)}  é {funções.dobro(preço)}')
print(f'A metade de {funções.moeda(preço)}  é {funções.metade(preço)}')

print()