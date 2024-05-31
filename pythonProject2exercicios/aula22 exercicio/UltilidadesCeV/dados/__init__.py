def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO!\t{entrada}\t não é um preço valido.\033[m')
        else:
            válido = True
            return float(entrada)


def leiaInt(msg):
    válido = False
    valor = 0
    while not válido:
        entrada = str(input(msg))
        if entrada.isnumeric():
            valor = int(entrada)
            válido = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro valido\033[m.')


