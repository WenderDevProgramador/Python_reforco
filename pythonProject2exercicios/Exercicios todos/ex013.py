produto=float(input('Qual é o preço do produto ? R$ '))
final=produto-(produto*5/100)
print('O produto custa R$ {} e você tem mais 5% de desconto. O valor com desconto é  R${:.2f}'.format(produto,final))
