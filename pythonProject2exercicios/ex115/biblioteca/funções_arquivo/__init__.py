from ex115.biblioteca.funções import *

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        return False
    else:
        return True


def LerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        titulo('VER PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro! Não conseguimos abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            print(f'Registro {nome} foi adicionado.')
        except:
            print('Erro! Não coseguimos cadastrar pessoa.')
    finally:
        a.close()
