#Exercício Python 73:
# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação.
# Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

tabela = ('vitoria', 'criciuma','novorizonte','sport','juventude',
          'atletico goianiense','vila nova','mirassol','guarani',
          'crb','ceara','botafog','avai','ituano','ponte preta',
          'sampaio','tombense','chapecoense','londrina','abc')
print(f'Os cinco primeiros times são {tabela[0:5]}')
print(f'Os quatro ultimos colocados são {tabela[-4:]}')
print(f'Os times em ordem alfabetica são {sorted(tabela)}')

print(f'O clube chapecoense esta na posição {tabela.index("chapecoense")+1}º')