"""
Enunciado:

Faça uma função que receba um número N e retorne a soma dos algarismos de N!. Ex: se N = 4, N! = 24. Logo, a soma de
seus algarismos é 2 + 4 = 6
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


def soma_algarismos(n):
    """
    Soma os algarismos de um número
    :param n: numero
    :return: Retorna a soma dos algarismos do número
    """

    # Calcula o fatorial do número primeiro
    fatorial_num = fatorial(n)

    soma = 0
    # Separa os últimos digitos do número até não ser mais possível dividir
    while fatorial_num >= 10:
        soma = soma + fatorial_num % 10
        fatorial_num = int(fatorial_num/10)
    soma = soma + fatorial_num
    return soma


num = int(input('Digite um número n '))
print(f'O fatorial de {num} é {fatorial(num)}. Logo, a soma de seus algarismos é {soma_algarismos(num)}')


