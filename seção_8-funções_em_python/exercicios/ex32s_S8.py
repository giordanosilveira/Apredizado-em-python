"""
Enunciado:

Faça uma função chamada 'simplifica' que recebe como parâmetro o numerador e o denominador de uma fração. Esta função
dever simplicar a fração recebida dividindo o numerador e o denominador pelo maior falor possível. Por exemplo, a fração
36/60 simplifica para 3/5 dividindo o numerador e o denominador por 12. A função deve modificar as variáveis passadas
como parâmetro.
"""


def simplifica(numerador, denominador):
    """
    Simplifica o numerador e o denominador de uma função
    :param numerador: Numerador de uma função
    :param denominador: Denominador de uma função
    :return: mostra a função simplificada e o maior denominador comum entre o numerador e o denominador
    """
    menor_numero = min(numerador, denominador)

    # Do menor número entre o numerador e o denominador até 1
    for i in range(menor_numero, 1, -1):

        # Caso ache um número que divide simultaneamente numerador e denominador, para o loop e retorna a mensagem
        if numerador % i == 0 and denominador % i == 0:
            return f"A função {numerador}/{denominador} é simplificada para {int(numerador/i)}/{int(denominador/i)}. " \
                   f"O maior divisor dos números é {i}"

    # Caso não ache nenhum número que divida os dois ao mesmo tempo, o MDC é 1
    return f"A função {numerador}/{denominador} é simplificada para {int(numerador/1)}/{int(denominador/1)}. " \
           f"O maior divisor dos números é {1}"


print('Escreva o numerador e o denominador da fração que você deseja simplificar')
print(simplifica(int(input()), int(input())))

