def leiaDinheiro(v):
    número = False
    num = 0
    
    while not número:
        valor = str(input(v)).strip().replace(',','.')
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mERRO!"{valor}" não é valido.\033[0m')
        else:
            num = float(valor)
            número = True
            
    return  num

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


def leiaFloat(msg):
    while True:
        
        try:
            n = float(input(msg))
            
        except(KeyError,ValueError,TypeError):
            print('\033[1;31m ERRO! Digite um número inteiro valido\033[m')
            continue
        
        except(KeyboardInterrupt):
            print('Usuário preferio não inserir valor!')
            n = 0
            return n
            break
        
        except:
            print(f'\033[1;31mERRO ao digitar valor!\033[m')
            continue
        
        else:
            return n
            
            
        