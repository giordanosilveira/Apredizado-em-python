"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que foi vista em listas. O sort() só funciona em listas. Podemos
usar o sorted() para qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted() sempre retorna uma lista com os elementos do iterável ordenados. Ele não modifica a lista passada

# Exemplo
numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))  # Ordenar do menor para o maior
print(numeros)

# Adicionando parâmetros ao sorted()
numeros = [4, 2, 6, 1]
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted() para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]
print(usuarios)

# Ordenando pelo "username"
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""
# ultimo exemplo
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in BLack", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

# Da menos para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Da mais para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))


