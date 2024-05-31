#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
# a)Quantos números foram digitados. 
# b)A lista de valores, ordenadas de forma decrescente.
# c)Se o valor 5 foi digitado e se está ou não na lista.
 
print(' ')
num = []
while True:
    n = int(input('Digite um número para cadastrar: '))
    num.append(n)
    c = str(input('Deseja continuar a cadastrar? S/N ')).upper().strip()[0]
    if c == 'N':
        break
print(' ')
print(f'Foram adicionados a lista um total de {len(num)} números.')
num.sort(reverse=True)
print(f'Os valores da lista em ordem decrescente é {num}.')
if 5 in num:
    print(f'O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')   
print(' ')