"""
Reversed

OBS: não confunda com a função reverse() que estudamos nas listas
A função reverse() só funciona com listas.
Já a função reversed() funciona com qualquer iterável.
Sua função é inverter o iterável
A função reversed() retorna um iterável chamado list_reverseiterator

"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornando para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto
# OBS: Em conjunto, não definimos a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Giordano Henrique Silveira'):
    print(letra, end='')

print()

# Podemos fazer o mesmo sem o uso do foor
print(''.join(list(reversed('Giordano Henrique Silveira'))))
print('Giordano Henrique Silveira'[::-1])  # Slice

# Podemos também utilizar o reversed() par fazer um loop reverso
for n in reversed(range(0, 10)):
    print(n, end='')

print()

# Apesar que também já vimos como utilizar o próprio range para fazer isso
for n in (range(9, -1, -1)):
    print(n, end='')