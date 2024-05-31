#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre: 
#a)Quantas pessoas foram cadastradas.
#b)Uma listagem com as pessoas mais pesadas.
#c)Uma listagem com as pessoas mais leves.

print('  ')
princ = []
lista = []
maior = 0
menor = 9999999999999999999999999999999999999999
while True:
    nome = str(input('Nome: ')).title().strip()
    peso = float(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    princ.append(lista[:])
    lista.clear()
    while True:
        c = str(input('Cadastrar mais? [S/N]')).upper().strip()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
print('   ---> PESSOAS CADASTRADAS.')
print('   ')
for pos in range(0,len(princ)):
    if princ[pos][1] == 0:
        maior = menor = princ[pos][1]
    else:
        if princ[pos][1] > maior:
            maior = princ[pos][1]
        if princ[pos][1] < menor:
            menor = princ[pos][1]

for pos in range(0,len(princ)): 
    print('-'*30)     
    print(f'NOME: {princ[pos][0]}')
    print(f'PESO: {princ[pos][1]}')
    
print('   ')  
print(f'Foram cadastradas o total de {len(princ)} pessoas.')
print('   ')
print(f'As pessoas mais pesadas tem {maior}KG e pertecem á, ',end=' ')
for pos in range(0,len(princ)): 
    if princ[pos][1] == maior:
        print(f'{princ[pos][0]}',end='...')
print('   ')
print(f'\nAs pessoas mais leves tem {menor} e pertencem á, ',end=' ')
for pos in range(0,len(princ)): 
    if princ[pos][1] == menor:      
        print(f'{princ[pos][0]}',end='...')
print('\nFim')