"""
Funções com retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f' Retorno de pop {ret_pop}')
print(numeros)

ret_pr = print(numeros)
print(f'Retorno de print{ret_pr}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None
OBS 2: Funções Python que retornam valores, devem retornar esses valores com a palavra reservada 'return'
OBS 3: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução
da função para outras funções.

# Exemplo função sem retorno
# def quadrado_de_7():
    # print(7 * 7)

# Vamos refatorar essa função para que ela retorne o valor


def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'O retorno de ret {ret}')
print(f'O resultado é {quadrado_de_7() + 1}')

# Refatorando o diz_oi ()
def diz_oi():
    return 'Oi, '


print(diz_oi())

alguem = 'Giordano!'
print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return
- Ela finaliza a função, ou seja, ela sai da execução da função;
# Exemplo 1
def diz_oi():
    print('Estou sendo executado antes do retorno')
    return 'Oi!'
    print('Estou sendo executado após o retorno')
print(diz_oi())

- Podemos ter, em uma função, diferentes returns;
# Exemplo 2
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

- Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores
# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda
from random import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(f'O valor da moeda é {joga_moeda()}')

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária


def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
"""

