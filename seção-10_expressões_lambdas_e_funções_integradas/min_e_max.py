"""
Min e Max:

max -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos
lista = [1, 8, 4, 99, 32, 129]
print(max(lista))  # 129

tupla = 1, 8, 4, 99, 32, 129
print(max(tupla))  # 129

conj = {1, 8, 4, 99, 32, 129}
print(max(conj))  # 129

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 32, 'f': 129}
print(max(dict))  # f

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 32, 'f': 129}
print(max(dict.values()))  # 129

# Faça um programa que receba dois valores do usuário e mostre o maior valor
val1 = int(input())
val2 = int(input())

print(max(val1, val2))

# Pode passar qualquer tipo de valor para o max()

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplos
lista = [1, 8, 4, 99, 32, 129]
print(min(lista))  # 1

tupla = 1, 8, 4, 99, 32, 129
print(min(tupla))  # 1

conj = {1, 8, 4, 99, 32, 129}
print(min(conj))  # 1

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 32, 'f': 129}
print(min(dict))  # a

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 32, 'f': 129}
print(min(dict.values()))  # 1

# Faça um programa que receba dois valores do usuário e mostre o menor valor
val1 = int(input())
val2 = int(input())

print(min(val1, val2))

# Outros exemplos
nomes = 'Arya Samsom Dora Tim Olivander'
nomes = list(nomes.split(' '))

max e min pelo primeiro caractere"
print(max(nomes))
print(min(nomes))

max e min pelo número de caracteres
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
"""
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in BLack", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio: Imprima somente o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?
maior = 0
for i in range(len(musicas)):
    if musicas[i]['tocou'] > maior:
        maior = i
print(musicas[maior])
print(musicas[maior]['titulo'])

menor = musicas[0]['tocou']
i = 1
for i in range(len(musicas)):
    if musicas[i]['tocou'] < menor:
        menor = i
print(musicas[menor])
print(musicas[menor]['titulo'])
