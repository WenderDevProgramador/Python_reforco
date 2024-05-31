#Ordem de precedência para equações:
#1()
#2**
#3*,/,//,%
#4+-
n1=int(input('Digite um numero:'))
n2=int(input('Digite outro numero:'))
#pode ser colocar s=n1+n2 ou da forma aseguir
#print('A soma é igual á {}:'.format(n1+n2))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
#print('A soma é {},\n a multiplicação é {} ,\n a divisão é {:.3f} \n '.format(s,m,d),end=' ')
#print('A divisão inteira é {}\n e a potencia é {}'.format(di,e))
print('A soma é {}, a multiplicação é {} , a divisão é {:.3f}  '.format(s,m,d),end=' ')
print('A divisão inteira é {} e a potencia é {}'.format(di,e))