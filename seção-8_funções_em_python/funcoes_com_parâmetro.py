"""
Funções com Parâmetros

- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamentos saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada
- Não possuem saída
- Possuem entrada, mas não possuem saida
- Não possuem entrada, mas possuem saída
- Possuem entrada e possuem saída

# Refatorando uma função
def quadrado(numero):
    # return numero * numero
    return numero ** 2


# print(quadrado())  # TypeError
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva {aniversariante}, porra!')


aniversariante = 'a Patrícia'
cantar_parabens(aniversariante)

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada em uma função quanto parâmetros forem
# necessários. Eles são separados por ','.

# Exemplos


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(5, 2))
print(soma(10, 20))
print(multiplica(4, 5))
print(multiplica(2, 8))
print(outra(3, 2, 'Giordano '))
print(outra(5, 4, 'GG '))

# OBS: Se a gente informar um número errado de parâmetro/argumento teremos TypeError
# print(soma(1, 2, 3))  # TypeError, passando argumentos a mais
print(soma(2))  # TypeError, passando argumentos a menos

# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Giordano Henrique', 'Silveira'))

# A diferença de parâmetros e argumentos:
# Parâmtros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!
nome = 'Jessica'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para irformá-los, podemos utilizar qualquer ordem
print(nome_completo(nome='Jessica', sobrenome='Jones'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome=sobrenome, nome=nome))

# Erro comum na utilização do return


def soma_impares(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 1:
            soma = soma + num
    return soma


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(soma_impares(numeros))

tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(soma_impares(numeros))
"""


