def linha(tam=42):
    return '-'*tam


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(n):
    while True:
        try:
            l = int(input(n))
        except:
            print('\033[31;mERRO! Insira um número inteiro valido.')
        else:
            return l
            break


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for o in lista:
        print(f'{c} \033[33m- {o}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Digite sua opção: ')
    return opc
