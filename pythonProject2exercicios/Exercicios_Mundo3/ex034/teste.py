#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),diminuir(),dobro() e metade().Faça também um programa que importe esse modulo e use algumas dessas funções.

import moeda

print()

preço = float(input('Digite um preço R$: '))

print(f'O preço com um aumento para compra a prazo  fica R$ {moeda.aumentar(preço,5):.2f}')
print(f'O preço com um desconto  para pagamento avista fica R$ {moeda.diminuir(preço,5):.2f}')
print(f'O dobro do valor é R$ {moeda.dobro(preço):.2f}')
print(f'A metade do valor é R$ {moeda.metade(preço):.2f}')

print()
