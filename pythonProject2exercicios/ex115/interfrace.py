from ex115.biblioteca.funções import *
from ex115.biblioteca.funções_arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)




while True:
    resposta = menu(['VER PESSOAS CADASTRADAS','CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        # Ver pessoas cadastradas.
        LerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        # Cadastrar uma nova pessoa.
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).title().strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
        sleep(1)
    elif resposta == 3:
        # Sair do sistema.
        print('Saindo do sistema . . .')
        sleep(1)
        break
    else:
        print('\033[32mNão existe essa opção digite uma opção valida!\033[m')
        sleep(2)

