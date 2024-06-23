#Dentro do pacote ultilidades que criamos no desafio anterior, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar com a função input(), mas com uma validação de dados para aceitar apenas valores que sejá monetários.


print('  ')
from ultilidades import preço,dados

a = dados.leiaDinheiro('Digite o valor: R$ ')
preço.resumo(a)


print('  ')