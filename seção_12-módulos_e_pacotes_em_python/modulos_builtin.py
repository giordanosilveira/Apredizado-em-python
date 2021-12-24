"""
Trabalhando com módulos built-in (módulos integrados, que já vem instalados no Python)

____________________________
|python|Módulos built-in|
----------------------------

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o '*'
from random import *
print(random())

# Importando todo o módulo
import random
print(random.random())

# utilizando alias (apelidos) para módulos/função
from random import randint as rdi
print(rdi(5, 89))

# utilizando alias (apelidos) para módulos/função
from random import randint as rdi, random as rdn
print(rdi(5, 89))
print(rdn())

https://docs.python.org/3/py-modindex.html
"""

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())
print(randint(3, 7))
lista = ['Giordano', 'Henrique', 'Silveira']
shuffle(lista)
print(lista)

print(choice('Giordano'))

