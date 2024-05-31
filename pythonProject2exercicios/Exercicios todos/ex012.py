altura=float(input('Qual a altura da parede ? '))
largura=float(input('Qual é a largura da parede ? '))
area=altura*largura
print('As medidas da parede são {:.2f} x {:.2f} e tem uma dimensão de {:.2f} m²'.format(altura,largura,area))
tinta=area/2
print('Para pintar essa parede você precisara de {:.2f} L de tinta '.format(area))
