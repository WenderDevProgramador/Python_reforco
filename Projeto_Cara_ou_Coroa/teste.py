print('Cadastro de pessoas!!')
continua = ' '
while continua != 'não':

    a = str(input('Qual é o seu nome? '))
    print(f'O seu nome é {a}.')
    b = int(input('Qual a sua idade? '))
    print(f'A sua idade é {b}.')
    continua = str(input('Deseja cadastrar mais pessoas? '))
    
print('Cadastros realizados com sucesso.')