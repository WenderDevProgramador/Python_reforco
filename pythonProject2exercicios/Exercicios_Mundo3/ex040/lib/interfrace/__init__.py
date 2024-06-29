

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError,ValueError,KeyError):
            print('\033[1;31m ERRO! Digite um número inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferio não inserir valor!')
            n = 0
            return n
            break
        except:
            print(f'\033[1;31mERRO ao digitar valor!\033[m')
            continue
        else:
            return n

def linha(tam=42):
    return '-' * tam
    
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for v,item in enumerate(lista):
        print(f'\033[1;33m{v+1} - \033[0;34m{item}\033[m')
    print(linha())
    opc = leiaInt('Digite sua opção: ')
    
    return opc