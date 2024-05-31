from time import sleep
km=int(input('Quantos km vai percorrer na viagem ? '))
print('Lembrando que para viagens acima de 200 km o preço sera R$0.45 por km '
      'e abaixo disso R$0.50 preço normal')
sleep(5)
if km <=200:
    print('Você ira pagar R${:.2f} pela viagem.'.format(km*0.50))
else: print('Você ira pagar R${:.2f} pela viagem.'.format(km*0.45))
