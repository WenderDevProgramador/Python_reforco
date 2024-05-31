#Faça um programa que leia nome e média de um aluno,
#guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.
print('   ')
aluno = {}

aluno['NOME:'] = str(input('NOME: ')).strip().upper() 
aluno['MEDIA:'] = float(input('MÉDIA: '))
if aluno['MEDIA:'] < 5:
    aluno['SITUAÇÃO:'] = 'REPROVADO'
elif aluno['MEDIA:'] >= 5 and aluno['MEDIA:'] < 7:
    aluno['SITUAÇÃO:'] = 'EM RECUPERAÇÃO'
else:
    aluno['SITUAÇÃO:'] = 'APROVADO'
print('-='*30)    

for k, d in aluno.items():
    print(f' {k}   {d}')
    
print('-='*30)     