"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = 1, 2, 3
print(tupla[1])

Named Tuple -> São tuplas diferenciadas as quais especificamos um nome para a mesma e também parâmetros

# Precisamos definir o nome e parâmetros

# Forma 1:
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2:
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando
adilson = cachorro(idade=2, raça='Bulldog', nome='Adilson')
print(adilson)

# Acessando os dados

# Forma 1
print(adilson[0])  # Idade
print(adilson[1])  # raça
print(adilson[2])  # nome

# Forma 2
print(adilson.idade)  # Idade
print(adilson.raça)  # raça
print(adilson.nome)  # nome

"""

from collections import namedtuple


print(adilson.index('Bulldog'))
print(adilson.count('Bulldog'))
