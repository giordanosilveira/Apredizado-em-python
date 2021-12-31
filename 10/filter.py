"""
Filter

filter() -> server para filtrar dados de uma determinada coleção

valores = 1, 2, 3, 4, 5, 6
media = sum(valores)/len(valores)
print(media)

# lib para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma uma função e um iterável
res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))
print(f'Novamente: {list(res)}')

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# A diferença entre map e filter é:
# Na map() -> recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
# elemento do iterável

# O filter() -> Recebe dois parâmetros, um função e um iterável e retorna um objeto filtrando apenas os elementos de
# acordo com a função

# Exemplo mais complexo
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "Gal", "tweets": []},
]
print(usuarios)

# Filtrar os usuários que estão inativos no Twitter
# Forma 1
# inativos = list(filter(lambda x: x["tweets"] == list(), usuarios))
# print(inativos)

# Forma 2
# inativos = list(filter(lambda x: len(x["tweets"]) == 0, usuarios))
# print(inativos)

# Forma 3
inativos = list(filter(lambda x: not x["tweets"], usuarios))
print(inativos)
"""
# Combinar map() e filter()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo sua 'Sua estrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
instrutores = list(map(lambda x: f'Sua instrutora é {x}', filter(lambda x: len(x) < 5, nomes)))
print(instrutores)
