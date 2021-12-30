"""
Enunciado:

Faça uma função que retorne o maior fator primo de um número
"""

from math import sqrt


def testa_numero():
    """
    Teste para verificar se o usuário digitou um número inteiro
    :return: O número que o usuário digitou
    """
    eh_valido = False
    print('Digite um número inteiro')

    # Enquanto não for digitado um valor válido, permanece no laço
    while not eh_valido:
        try:
            num = int(input())
        except ValueError:
            print(f'Não foi digitado um número inteiro. Digite um inteiro')
        else:
            eh_valido = True
    return num


def eh_primo(divisor):

    """
    Verifica se o divisor é um número primo
    :param divisor: possível divisor
    :return: 1 se o número for primo, 0 senão for
    """

    maior_divisor = int(sqrt(divisor))
    # É necessário verificar até a raiz quadrada de um número para ver se é primo
    for i in range(2, maior_divisor + 1):
        #breakpoint()

        # Se for divisível por algum número, não é primo
        if divisor % i == 0:
            # breakpoint()
            return 0
    return 1


def fatores_primo(num):

    """
    Função que calcula os fatores primos de um número
    :param num: Número que vai ser calculado os fatores primos
    :return: O maior fator primo do número
    """

    # Verificação para ver se num é primo, se sim, retorna ele mesmo
    if eh_primo(num):
        return num

    # Usando um conjunto porque ele não admite números repetidos. Além disso, eu só preciso do maior fator primo.
    primos = {1}
    i = 2

    # A medida que vou diminuindo o número o número de volta no laço é menor
    while i <= num:

        # Se o divisor for primo
        if eh_primo(i):

            # se o número for divisível por i, adiciona ele no conjunto, ele não será incluído se tiver um repetido
            # por causa das regras do conjunto
            if num % i == 0:
                num = num/i
                primos.add(i)
            # Caso não seja divisível, tenta o próximo número
            else:
                i += 1

        # Caso não seja primo, tenta o próximo número
        else:
            i += 1

    # Retorna o valor máximo do conjunto
    return max(primos)



numero = testa_numero()
print(f'O maior fator primo do numero {numero} é {fatores_primo(numero)}')

