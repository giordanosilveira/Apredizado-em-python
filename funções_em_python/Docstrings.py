"""
Documentando funções com o Docstrings

OBS: Podemos ter acesso a uma documentação em de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda ter acesso à Documentação com a função help()
"""
# Exemplos


def diz_oi():
    """uma função simples que retorna a string oi"""
    return 'Oi '


def exponencial (numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de um número, ou o número à potencia informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponêncial de numero ** potencia.
    """
    return numero ** potencia


