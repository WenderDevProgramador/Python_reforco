#Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# EX: 
# n=leiaInt('Digite um número')

def leiaInt(msg):
   ok = False
   valor = 0
   while True:
       n = input(msg)
       if n.isnumeric():
           valor = int(n)
           ok = True
       else:
           print('\033[31m Erro !! Digite um número inteiro valido!!\033[m') 
       if ok:
           break
   return valor
   
print('  ')
n = leiaInt('Digite um Número para validar: ') 

print(f'O número que você digitou foi {n} .')
print('  ')