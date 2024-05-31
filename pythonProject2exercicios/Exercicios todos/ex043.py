from datetime import date
#Faça um programa que leia o ano de
# nascimento de um jovem e informe,
# de acordo com a sua idade, se ele
# ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já
# passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

ano=int(input('Digite o ano em que você nasceu: '))
sexo=int(input('''Digite a opção abaixo:
 [1]Para feminino 
 [2]Para masculino'''))

atual = date.today().year
idade = atual - ano
print('Quem nasceu em',ano, 'tem',idade,'anos em',atual)
if idade == 18 and sexo==2:
    print('Você tem que se alistar "IMEDIATAMENTE" procure a junta militar mais proxima')
elif idade < 18 and sexo==2:
    print('Você ainda não tem 18 anos. Ainda falta {} para o seu alistamento.'.format(18 - idade))
    print('Seu ano de alistamento será em {}'.format((18 - idade)+atual))
elif idade > 18 and sexo==2:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu ano correto de se alistar foi em {}'.format(atual-(idade-18)))
else:
    print('Você é do sexo feminino seu alistamento não é obrigatorio!')
