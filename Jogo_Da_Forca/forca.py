#Jogo da forca.

from resposta import palavra
from random import choice

palavra_sorteada = choice(palavra)
tentativas = []
chances = 7



print('  ')
print(f'='*60)
print(f'{"JOGO DA FORCA":=^60}')
print(f'='*60)
print('  ')
print(f'TENTE ADIVINHAR A PALAVRA COM {len(palavra_sorteada)} letras.')
print('  ')
while True:
    for letra in palavra_sorteada:
        if letra in tentativas:
            print(letra,end=' ')
        
        else:
            print('-',end=' ')
        
        
    letra = str(input('Digite uma letra: ')).strip().lower()[0]
    if letra in tentativas:
        print('Letra repetida tente outra.') 
    for l in palavra_sorteada:
        if letra == l:
            tentativas.append(letra)      
        
    if letra not in palavra_sorteada:
        chances -= 1
        print(f'Errou !!   Você tem ainda {chances} chances para acerta. . .')
        print(' ')
    
        
    print(' ')
    
    if len(tentativas) == len(palavra_sorteada):
                print(f'Você ganhou !! A palavra é {palavra_sorteada.upper()}!!')
                break
         
    if chances == 0 :
        print(f'GAME OVER!! Chances esgotadas a palavra é {palavra_sorteada.upper()}')
        break
    
            
    
print('  ')