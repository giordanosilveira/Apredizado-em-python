"""
Utilizando lambdas

Conhecidadas por expressões lambdas, ou simplesmente lambdas, são funções sem nomes, ou seja, funções anônimas.

#Função em python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda ?
calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(5))

# Podemos ter expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Giordano Henrique', 'silveira'))
print(nome_completo('  giordano henrique ', ' SILVEIRA '))
print(nome_completo('  GIORDANO HENRIQUE         ', 'SILVEIRA '))


# Em funções python podemos ter nenhuma ou várias entradas. Em lambdas também
amar = lambda: 'Como não armar Python? '
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: (3 / (1/x + 1/y + 1/z))
# n = lambda x1, x2, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
# OBS: Se passamos mais parâmetros do que argumentos teremos TypeError

# Outros exemplos
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Definindo a função
def geradora_funcao_quadratica(a, b, c):
        Retorna a função f(x) = a*x^2 + b*x + c
    return lambda x: a*x**2 + b*x + c

teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

Usamos lambdas para fazer filtragens ou ordenação de dados
"""


