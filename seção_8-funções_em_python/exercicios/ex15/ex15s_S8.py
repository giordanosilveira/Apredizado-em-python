"""
Enunciado:

No print da pasta
"""


def eh_triangulo():
    """
    Função que recebe os dados do usuário e verifica se é triângulo
    :return: A lista que contém os tamanho dos lados se for triângulo. Caso não seja, volta uma lista vazia
    """
    lados = []
    print('Digite os tamanho dos lado do triângulo')
    lados.append(int(input()))
    lados.append(int(input()))
    lados.append(int(input()))

    # Regra para verificar se é triângulo
    # A soma de dois lados tem que ser maior que o terceiro lado
    if lados[0] + lados[1] > lados[2]:
        if lados[1] + lados[2] > lados[0]:
            if lados[0] + lados[2] > lados[1]:
                return lados
            else:
                return []
        else:
            return []
    return []


def qual_triangulo(lados):
    """
    Verifica qual triângulo ele é. Se é isóceles, equilátero ou escaleno
    :param lados: Lista que contém o tamanho dos lados do triângulo
    :return: Qual triângulo é
    """
    # Se a = b e a = c, consequentemente b = c
    if lados[0] == lados[1] and lados[0] == lados[2]:
        return 'É um triângulo equilátero'
    # Se a != b e a != c, consequentemente b != c
    elif lados[0] != lados[1] and lados[0] != lados[2]:
        return 'É um triângulo escaleno'
    # Se algum lado for igual ao outro
    else:
        return 'É um triângulo isóceles'


lados = eh_triangulo()
# Se recebeu a lista com os lados
if lados:
    print(f'{qual_triangulo(lados)}')
else:
    print('Não é um triângulo')

