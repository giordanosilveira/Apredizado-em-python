"""
List Comprehension

- Utilizando list Comprehension nós podemos gerar novas lista com dados processados a partir de outro iterável.

# Sintaxe da list comprehension

[dado for dado in iterável]

# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

"""
"""
para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- segunda parte: numero * 10

res = [numero/2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(num) for num in numeros]
print(res)

# list comprehension x loops
# loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for num in numeros:
    numeros_dobrados.append(num*2)

print(numeros_dobrados)

# List comprehension
print([num * 2 for num in numeros])
"""

# Outros exemplos

# 1
nome = 'Giordano Henrique Silveira'
print([letra.upper() for letra in nome])

# 2
amigos = ['giba', 'carlos', 'jessica', 'madeline', 'jooj']
print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5, 6]])
