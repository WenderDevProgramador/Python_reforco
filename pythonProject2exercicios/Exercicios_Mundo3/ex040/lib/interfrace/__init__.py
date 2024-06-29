def linha(tam=42):
    return '-' * tam
    
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    print(lista)