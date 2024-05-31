#Crie um programa onde o usuário possa digitar varios valores númericos e cadastreos em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores
# únicos digitados , em ordem crescente.
print(' ')
lista = []

while True:
    n = int(input('Digite um número para cadastrar: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Número já cadastrado, digite outro número. ')
    continua = str(input('Deseja cadastrar mais número? [SIM/NÃO]  ')).upper().strip()[0]
    if continua == 'N':
        break
lista.sort()    
print(f'Números cadastrados {lista}.')
print(' ')
print('FIM >>> ')
print(' ')