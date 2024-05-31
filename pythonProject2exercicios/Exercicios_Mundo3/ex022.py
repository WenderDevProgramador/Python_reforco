#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cadda pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A)Quantas pessoas cadastradas.
# B)A média de idade.
# C)Uma lista com mulheres.
# D)Uma lista com idade acima da média.
print('  ')

lista = []
dicionario = {}
idade = 0

while True:
    dicionario.clear()
    dicionario["Nome:"] = str(input('Nome: ')).strip().upper()
    dicionario['Idade:'] = int(input('Idade: '))
    idade += dicionario['Idade:']
    
    while True:
        dicionario["Sexo:"] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if dicionario["Sexo:"] not in 'MF':
            print('Erro!! Digite M ou F.')
        else:
            break
    lista.append(dicionario.copy())
    cadastra = '  '
    while cadastra not in 'SN':
        cadastra = str(input('Cadastrar mais pessoas [S/N]? ')).strip().upper()[0]
        if cadastra not in 'SN':
            print('Erro ! Digite S ou N.')
    if cadastra == 'N':
        break
    
media = idade/len(lista)

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade das pessoas cadastradas é {media:.2f} anos.')
print('As mulheres cadastradas são ',end=' ')
for p in lista:
    if p["Sexo:"] == 'F':
        print(f'{p["Nome:"]}',end=', ')
print(' ')    

print('As pessoas com idade acima da media são:')  
for p in lista:
    if p["Idade:"] > media:
        for c , d in p.items():
            print(f'{c}  {d}',end=' ')
        print('  ')
print('   ')