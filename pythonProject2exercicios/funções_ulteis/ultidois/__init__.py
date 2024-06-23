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
