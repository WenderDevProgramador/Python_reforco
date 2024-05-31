#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*num):
    print('  ')
    from time import sleep
    cont = maior = 0
    print(f'Os números analisados são: ',end=' ')
    for n in num:
        print(f'{n}',end=' ',flush=True)
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'\nForam analisados {cont} números. E o maior entre eles é {maior}.')
    print('  ')
        
    

maior(4,5,6,7,8,1,2)
maior(1,2)
maior(10,50,2,100)
maior(-1,2,3,0)
maior()