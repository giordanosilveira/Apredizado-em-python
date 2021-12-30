"""
Enunciado:

No print da página
"""


def fatorial(n):
    """
    Calcula o fatorial de um número
    :param n: Número que vai ser calculado o fatorial
    :return: Retorna o fatorial de número
    """
    mult = 1
    for i in range(n):
        mult = mult * (i + 1)
    return mult


def graus_para_radiano(ang):
    """
    Converte um ângulo em graus para radiano
    :param ang: ângulo em graus
    :return: ângulo em radiano
    """
    pi = 3.141593
    return ang*(pi/180)


def seno_hiperbolico(angulo):
    """
    Calcula o seno hiperbólico de um ângulo em radianos segundo a fórmula pedida
    :param angulo: angulo em graus
    :return: o seno hiperbólico de um ângulo em radianos
    """
    radiano = graus_para_radiano(angulo)
    soma = radiano
    num = 3
    for i in range(2, 5 + 1):
        soma = soma + (radiano**num)/fatorial(num)
        num = num + 2
    return soma


angulo = float(input('Digite um ângulo em graus '))
print(f'O seno hiperbólico de {angulo}° variando de 0 à 5 é igual a {seno_hiperbolico(angulo)} ')
