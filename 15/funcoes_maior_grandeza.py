"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa? 
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumnetos para outras funções, e até mesmo criar variáveis do tipo funções nos nossos programas.

OBS: Na seção de funções, nós utlizamos isso.

Em python, as funções são Cidadões de Primeira Classe, First Class Citizer

# Exemplo - Definindo as funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# testando as funções
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# nested Functions - Funções Alinhadas
# Em Python podemos ter também funções dentro de funções, que são conhecidas por Nested Functions ou também Inner Functions (funções Internas)

# Exemplos
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai, ', 'Suma daqui, ', 'Gosto muito de você, '))
    return humor() + pessoa

# Testando
print(cumprimento('Angelina'))
print(cumprimento('Giordano'))

# Retornando funções de outras funções
from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahahahah', 'kkkkkkkkkk', 'hdsaudhauishduiahsdu'))
    return rir

rindo = faz_me_rir()
print(rindo())
"""

# inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas
from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        r = choice(('hahahahahaha', 'kkkkkkkkkkkkkkk', 'rsrsrsrsrsrsrsrs'))
        return f'{r} {pessoa}'
    return dando_risada


# Testando
rindo = faz_me_rir_novamente('Giordano')
print(rindo())
print(rindo())
print(rindo())
