"""
Módulo random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos em Python

Módulo random -> possui várias funções para a geração de números psedo-aleatórios

# Existe duas maneiras de se utilizar um módulo ou função deste
# Forma 1 - Importando todo o módulo (Não recomendado)

import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import de todo o módulo, todas as funções, classes, atributos e propriedades que estiverem dentro
# do módulo ficarão disponíveis (ficarão ná memória). Caso você saiba quais funções você precisa utilizar deste módulo,
# então esta forma 1 não seria a ideal de utilização.

print(random.random())

# Veja que para utilizar a função random() do módulo random, nós colocamos o nome do módulo e o nome  da função,
# separados por '.'

# OBS: não confunda a função random() com o módulo random. A random() é apenas uma função dentro do módulo

# Forma 2 - Importando uma função específica do módulo (Recomendado)
from random import random

# No import acima, estamos falando: do módulo random importe a função random()
for i in range(10):
    print(random())

# uniform() -> Gera um número pseudo-aleatório entre os valores estabelecido
from random import uniform

for i in range(10):
    print(uniform(3, 7))

# randint() -> Gera um número inteiro pseudo-aleatório entre os valores estabelecido
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')

# choice() -> pega um aleatório entre um iterável
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

# shuffle() -> tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(cartas)
shuffle(cartas)
print(cartas.pop())
"""
