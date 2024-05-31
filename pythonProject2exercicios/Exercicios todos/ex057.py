#Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite a frase: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverso =''
for letra in range(len(junta)-1,-1,-1):                   #inverso=junto[::-1]
    inverso = inverso + junta[letra]                      # essa alternativa de fatiamento é mais facil e mais rapido
print('A frase digitada de trás para frente: ')           # como a aula é de repetição usamos a outra alternativa.
print('{}  {}'.format(junta,inverso))
if junta == inverso :
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
