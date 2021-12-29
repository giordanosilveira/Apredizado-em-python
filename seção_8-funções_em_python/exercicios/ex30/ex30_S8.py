"""
Enunciado:

No print da pasta
"""


def testa_numero():
    """
    Teste para verificar se o usuário digitou um ângulo válido
    :return: O número que o usuário digitou
    """
    eh_valido = False
    print('Digite um ângulo em graus ')

    # Enquanto não for digitado um valor válido, permanece no laço
    while not eh_valido:
        try:
            num = input()
            num = float(num)
        except ValueError:
            print(f'Não foi digitado um ângulo válido. Digite um angulo')
        else:
            eh_valido = True
    return num


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


def cosseno_hiperbolico(angulo):
    """
    Calcula o cosseno hiperbólico de um ângulo em radianos segundo a fórmula pedida
    :param angulo: angulo em graus
    :return: o cosseno hiperbólico de um ângulo em radianos
    """
    radiano = graus_para_radiano(angulo)
    soma = 1
    num = 2
    for i in range(2, 5 + 1):
        soma = soma + (radiano**num)/fatorial(num)
        num = num + 2
    return soma


angulo = testa_numero()
print(f'O cosseno hiperbólico de {angulo}° variando de 0 à 5 é igual a {cosseno_hiperbolico(angulo)} ')
