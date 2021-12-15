"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas Comprehension
"""

# Exemplos

# 1
numeros = [1, 2, 3, 4, 5, 6]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 == 1]

print(pares)
print(impares)

# Refatorando
# Qualquer número par módulo 2 é 0 e 0 em Python é False. not False = True
pares = [num for num in numeros if not num % 2]
# Qualquer número impar módulo 2 é 1 e 1 em Python é True. not True = False
impares = [num for num in numeros if num % 2]

print(pares)
print(impares)

# 2
res = [num * 2 if num % 2 == 0 else num/2 for num in numeros]
print(res)
