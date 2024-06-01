#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
# - Quantidade de notas 
# - A maior nota 
# - A menor nota 
# - A média da turma 
# - A situação (opcional)
# Adicionar também as docstrings.

def notas(*n,Show=False):
    """Função para avaliar notas e situação de uma turma.
    :param *n: Recebe um ou varios valores de notas.
    
    Args:
        Show (bool, optional): Se for True irá mostrar a situação da turma.

    Returns:
        Retorna com um dicionario com os dados da nota da turma.
    """
    inf = {}
    nota = []
    for v in n:
        nota.append(v)
    inf["Notas"] = nota
    inf["Q Notas avaliadas"] = len(nota)
    inf["Maior nota"] = max(nota)
    inf["Menor nota"] = min(nota)
    inf["Média da turma"] = sum(nota) / len(nota)
    if  Show:
        if inf["Média da turma"] < 5:
            inf["Situação"] = 'Ruim'
        elif inf["Média da turma"] >= 5 and inf["Média da turma"] < 7:
            inf["Situação"] = 'Regular'
        else:
            inf["Situação"] = 'Boa'
        
    return inf

print('  ')
turma = notas(7.5,3,10,10,4.75,8.75,Show=True)
print(turma)
print('  ')
help(notas)    