#Crie um pequeno sistema modularizado que permite cadastrar passoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from lib.interfrace import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(['CADASTRAR PESSOAS','VER LISTA DE CADASTRO','SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastraPessoa(arq,nome,idade)
        
    elif resposta == 2:
        cabeçalho('VER LISTA DE CADASTRO')
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('OK. Saindo do sitema...')
        break
    else:
        print('\033[1;31mERRO! Opção invalida!\033[m')
    sleep(1)
        


