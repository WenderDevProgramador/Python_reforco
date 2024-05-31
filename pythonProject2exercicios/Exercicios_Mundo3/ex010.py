#Crie um programa que vai ler varios números e colocar em uma lista.
#Depois disso, 
#crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.
print(' ')
princ = []
par = []
impar = []

while True:
    n = int(input('Digite um número para cadastrar:  '))
    princ.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    c = str(input('Para continuar digite [S] para encerrar digite [N]: ')).upper().strip()[0]
    if c == 'N':
        break
print(' ')
print(f'Os números digitados foram {princ}.')
print(f'Os números pares digitados foram {par}.')
print(f'Os números impares digitados foram {impar}.')
print(' ')