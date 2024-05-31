nome=str(input('Qual é o seu nome ?')).title()
if nome == 'Wender':
    print('Que nome bonito!')
else:
    print('Seu nome é bem comum')
print('Bom dia!!{}'.format(nome))

n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite a sua segunda nota: '))
m=(n1+n2)/2
print('Sua primeira nota é {} a segunda é {}'.format(n1,n2))

print('Calculando sua media ...')
print('Sua media é {:.2f}'.format(m))
if m >=6:
    print('Você foi aprovado! Parabens !!')
else:
    print('Você foi reprovado, precisa estudar mais ...')
