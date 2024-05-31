''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''
from time import sleep
peso=float(input('Digite o seu peso: (KG)'))
altura=float(input('Digite a sua altura: (M)'))
imc=peso/(altura**2)
print('\033[1;31m Analizando o seu IMC ...\033[m')
sleep(2)
print('Seu peso é: {:.2f}'.format(peso))
print('Sua altura é: {:.2f} '.format(altura))
print('O seu IMC é: {:.2f}'.format(imc))
print('\033[1;31m Aguarde o resultado...\033[m')
sleep(4)
if imc <=17:
    print('Você está desnutrido!!')
elif imc >17 and imc <=18.5:
    print('Você está abaixo do peso!!')
elif imc > 18.5 and imc <=24.9:
    print('Você esta no peso normal!!')
elif imc > 25 and imc <= 29.9:
    print('Você esta acima do peso!! Faça uma dieta !')
elif imc >=30 :
    print('Você é obeso procure um medico para lhe ajudar seu gordo!!')
