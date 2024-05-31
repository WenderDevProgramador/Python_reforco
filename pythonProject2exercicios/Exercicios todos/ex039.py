print('\033[1;31m-=-=-=\033[m'*20)
print('Analisador de triângulos')
print('\033[1;31m-=-=-=\033[m'*20)
r1=float(input('Digite o comprimento um:'))
r2=float(input('Digite o comprimento dois:'))
r3=float(input('Digite o comprimento três :'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas acima \033[1;4;31m PODEM FORMAR TRIÂNGULO\033[m')
else:
    print('As medidas acima \033[1;4;31m NÃO PODEM FORMAR TRIÂNGULO\033[m')
#Para formar um triangulo o numero maoir não pode ser maior que a soma dos outros dois nuemros.
