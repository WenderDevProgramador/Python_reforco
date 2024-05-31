frase=str(input('Digite seu texto:')).strip().upper()
'Analisando o texto'
print('Texto digitado : {}'.format(frase))
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
#find essa função mostra aonde aparece a letra primeiro
#rfind mostra aonde apareceu a letra de tras para frente no texto
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1))
