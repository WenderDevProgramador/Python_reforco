#Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
ptermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão:'))
décimo = ptermo + (10 - 1) * razão
for c in range(ptermo, décimo + razão, razão):
    print(c,end=' --> ')
print('ACABOU!')
