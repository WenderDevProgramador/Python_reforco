#Crie um tupla preenchida com os 20 primeiros colocados da Tabela do campeonato brasileiro de futebol,na ordem de colocação, depois mostre: 
# a)Os cinco primeiros. 
# b)Os últimos quatro colocados. 
# c)Times em ordem alfabética.
# D)Em que posição está o time Flamengo. 

brasileiro_2019 = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco','Atlético-MG','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')

cont = 0

print('     -->Tabela Do Brasileiro De 2019.     <--')
print(' ')
for c in brasileiro_2019:
    print(f'{cont+1}º - {c}.')
    cont += 1

print('--'*40)

print(f'Os cinco primeiros colocados foram {brasileiro_2019[0:5]}.')
print(' ')
print('--'*40)
print(f'Os times rebaixados foram {brasileiro_2019[-4:]}.')
print(' ')
print('--'*40)
print(f'Os times em ordem alfabetica {sorted(brasileiro_2019)}.')
print(' ')
print('--'*40)
print(f'O Flamengo ficou na {brasileiro_2019.index("Flamengo")+1}ª posição.')
print(' ')
print('--'*40)
