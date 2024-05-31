#Exercício números por extenso.

print('='*60)
print('{:=^60}'.format('Números Por Extenso'))
print('='*60)


tupla = ("ZERO","UM","DOIS","TRÊS","QUATRO","CINCO","SEIS","SETE","OITO","NOVE","DEZ")


while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if  0 <= n <= 10:
        break
    print('Tente novamente.',end=' ')
print(f'Você digitou o número {tupla[n]}.')
