'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite o seu sexo. [ M/F ]: ')).strip().upper()[0]

while sexo not in 'MmfF':
    sexo = str(input('Dados invalidos. Por favor digite o sexo novamente [ M/F ]:')).strip().upper()[0]
print('Sexo {} resgitrado corretamente.'.format(sexo))
