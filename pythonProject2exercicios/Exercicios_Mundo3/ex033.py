#Faça um mini-sistema que ultilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: Use cores.

def ajuda(msg):
    titulo(f'Acessando o manual do {comando}. . .')
    help(msg)


def titulo(msg):
    tam = len(msg) + 4
    print('~'*tam)  
    print(f'  {msg}')
    print('~'*tam)
     

    
print('  ')    

while True:
    print('<<<< Sistema de ajuda PyHelp >>>>')
    comando = str(input('Digite Função ou Biblioteca:  '))
    
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('<<<<  Até logo  >>>>')

print('  ')  