"""
Enunciado:

Faça uma função não-recursiva que receba um número inteiro positivo N e retorne o superfatorial desse número. O
superfatorial de um número N é definido pelo produto dos N primeiros fatoriais de N. Assim, o superfatorial de 4 é
sf(4) = 1! * 2! * 3! * 4! = 288
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


def superfatorial(n):
    """
    Função que calcula o superfatorial de um número
    :param n: numero que será calculado o superfatorial
    :return: o superfatorial
    """
    mult = 1

    # Laço para calcular o superfatorial. n + 1 porque o limite do range é exclusivo
    for i in range(1, n + 1):
        mult = mult * fatorial(i)
    return mult


def testa_numero():
    """
    Teste para verificar se o usuário digitou um número válido
    :return: O número que o usuário digitou
    """
    eh_valido = False
    print('Digite um número inteiro positivo ')

    # Enquanto não for digitado um valor válido, permanece no laço
    while not eh_valido:
        try:
            num = input()
            num = int(num)
        except ValueError:
            print(f'Não foi digitado um número válido. Digite um número válido')
        else:
            if num >= 0:
                eh_valido = True
            else:
                print('O número digitado é menor que 0. Digite um número inteiro positivo')
    return num


num = testa_numero()
print(f'O superfatorial de {num} é {superfatorial(num)}')

