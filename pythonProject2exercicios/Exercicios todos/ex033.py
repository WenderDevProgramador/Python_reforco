v=int(input('Qual a velocidade registrada ?'))
if v>80:
    print('Você foi multado!')
    print('Você pagara uma multa no valor de R${:.2f}'.format((v-80)*7.00))
else:
    print('Você não foi multado')