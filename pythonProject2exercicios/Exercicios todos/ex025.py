nome=str(input('Digite seu nome : ')).strip()
'Analizando seu nome...'
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))

#strip() retira os espaços do começo e do final
#upper transforma as letras em maiúsculas
#lower transforma as letras em minúsculas
#len() faz a contagem das letras
#count() conta oque estiver dentro dos parentes em '' letras pontos e espaços
#split() separa a frase em palavras
#find ' ' acha o primero espaço e define a palavra



