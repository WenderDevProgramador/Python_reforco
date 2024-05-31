#Exercício Python 113:
# Reescreva a função leiaInt()
# que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('ERRO! Digite um número inteiro valido.')
            continue
        except(KeyboardInterrupt):
            print('O usuario preferio não inserir o valor.')
            return 0
        else:
            return n
            break


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Digite um número real valido.')
            continue
        except(KeyboardInterrupt):
            print('O usuario preferiu não inserir valor.')
            return 0
        else:
            return n
            break


núm = leiaInt('Digite um valor: ')
print(f'O número digitado foi {núm} .')
flo = leiaFloat('Digite um valor real: ')
print(f'O valor digitado foi {flo} .')
