"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for (int i = 0; i < limitador; i++)
    //execução do loop

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    numeros = range (1, 10)

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

print('\n')
# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

print('\n')

# Exemplo de for 3 (iterando sobre um range)

range (valor_inicial, valor final)

valor_final exclusivo

for numero in range(1, 10):
    print(numero)


# Enumerate:

((0, 'G'), (1, 'i'), (2, 'o'), (3, 'r'), (4, 'd'), (5, 'a'), ... (n, 'a'))

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
for _, letra in enumerate(nome):
    print(indice)

nome = 'Giordano Henrique silveira'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

#orginal: U+1F60D
#modificado: U0001F60D

emoji = 'U0001F60D'
for _ in range(3):
    for numero in range(1, 11):
        print('\U0001F60D' * numero)
"""

