"""
Enunciado:

Escreva uma função que receba um número inteiro maior que 0 e retorne a soma de todos os seu algarismos. Por exemplo,
ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior que 0, o programa terminará com
a mensagem "Número Inválido"
"""


def soma_algarismos():
    """
    Soma os algarismos de um número
    :return: Retorna o a soma dos algarismos
    """
    numero = int(input('digite um número: '))
    soma = 0
    aux = numero

    # Enquanto o número for maior que 10
    while numero >= 10:

        # Separa o último digito do número e os soma
        soma = soma + numero % 10
        numero = int(numero/10)

    # Soma o primeiro dígito do número acima. Já que ele saiu antes de ser somado no laço acima
    soma = soma + numero

    return soma, aux


retorno = soma_algarismos()
print(f'A soma do número {retorno[1]} é {retorno[0]}')


