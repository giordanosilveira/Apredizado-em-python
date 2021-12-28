"""
Enunciado:

Faça uma função que receba uma temperatura em graus celciuls e retorne-a convertida em graus Fahrenheit. A
fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenhenit e C em graus celcius.
"""


def celcius_to_fahrenhenit(temperatura):
    """
    Converte a temperatura em graus celcius em fahrenreit
    :param temperatura: Temperatura em gruas celcius
    :return: temperatura em graus fahrenreit
    """
    return temperatura * (9.0/5.0) + 32.0


t_celcius = float(input('Temperatura em graus celcius '))
print(f'A temperatura em graus celcius {t_celcius} '
      f'e em graus Fahrenheit {celcius_to_fahrenhenit(t_celcius)}')



