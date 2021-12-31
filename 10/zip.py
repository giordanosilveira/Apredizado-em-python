"""
Zip

zip() -> Cria um iterável (zip object) que agreda cada um dos iteráveis passados como entradas em pares.

# Exemplos
lista = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista, lista2, 'abv')
print(zip1)
print(type(zip1))

# Sempre podemos gerar um lista, tupla, conjunto ou dicionário
# OBS: depois da primeira utilização, ele some da memória
print(list(zip1))

zip1 = zip(lista, lista2)
print(set(zip1))

zip1 = zip(lista, lista2)
print(tuple(zip1))

# OBS: o zip utiliza como parâmtro o menor tamanho em iterável. Isso significa que se estiver trabalhando com iteráveis
# de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com o zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dici = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'd': 15}

z = zip(tupla, lista, dici.values())
print(list(z))

# lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
"""

# Exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
