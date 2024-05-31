#Exercício Python 105:
# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*n,sit=False):
    """
    --> Ler notas e entregar paramentros.
    :param n: Adicionar valores das notas que precisar.ex(1,2,3,...)
    :param sit: Para adicionar situação da media ex: "BOM" , "RUIM"...
    :return: Retorna com o dicionario com os parametros.
    """


    dicio = {}
    dicio['TOTAL NOTAS'] = len(n)
    dicio['MAIOR '] = max(n)
    dicio['MENOR '] = min(n)
    dicio['MEDIA '] = sum(n)/len(n)
    if sit==True:
        if dicio['MEDIA '] <= 5:
            dicio['SITUAÇÃO'] = 'RUIM'
        elif dicio['MEDIA '] > 5 and dicio['MEDIA ']< 7:
            dicio['SITUAÇÃO'] = 'BOA'
        elif dicio['MEDIA '] > 7:
            dicio['SITUAÇÃO'] = 'OTIMA'

    return dicio



resp = notas(7,10,6,10,5,6,7,sit=True)
help(notas)




