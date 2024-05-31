#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo.Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1 
# b)De 10 até 0, de 2 em 2 
# c)Uma contagem personalizada

def contador(i,f,p):
    from time import sleep
    if p < 0:
        p*= -1
    if p == 0:
        p == 1
    print('  ')
    print(f'Iniciando de {i} contando {p} em {p} até {f}: ')
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.1)
            cont += p   
        print('FIM > > >')
        print('-='*20)
    if i > f:
        while cont > f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.1)
            cont -= p    
        print('FIM > > >')
        print('-='*20)
    
contador(1,30,1)
contador(50,0,5)

ini = int(input('Inicio: '))
fim = int(input('Final: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)