a=int(input('Digite o primeiro numero:'))
b=int(input('Digite o segundo numero:'))
c=int(input('Digite o terceiro numero:'))
#verificando quem é o menor:
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
print('O menor numero é {}'.format(menor))
#verificando o maior numero:
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O numero maior é {}'.format(maior))