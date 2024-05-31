'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
media=(n1+n2)/2
print('Sua media é', media)

if media < 5 :
    print('\033[1;31m Você foi REPROVADO estude mais no proximo ano\033[m')
elif 5.0 <= media <= 6.9:
    print('\033[1;m Você está de RECUPERAÇÃO!\033[m')
else:
    print('\033[1;34m Você foi APROVADO !! \033[m')
