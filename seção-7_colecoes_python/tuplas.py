"""
Tuplas (tuple)

Tuplas são bastantes parecidas com listas.

Existem basicamente duas diferenças básica
1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tuplas ela não muda. Toda operação em uma tuplas
gera uma nova tupla.

print(type(()))
# Cuidado 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6 #  -> Isso é uma forma de declarar uma tupla
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4) # Isso não é uma tuplas, mas sim um inteiro
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 5,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses
# Podemos gerar uma tupla dinamicamente com range(início, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar
tupla = ('Giordano', 'Silveira')
nome1, nome2 = tupla
print(nome1)
print(nome2)

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma* , Valor máximo*, Valor mínimo*, tamanho
# * valores inteiros, ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tuplas
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla.count('a'))

# Convertendo uma string para uma tupla e vice-versa
nome = tuple('Giordano Silveira')
print(nome)
print(type(nome))

nome2 = ''.join(nome)
print(nome2)
print(type(nome2))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O Acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i], end=' ')
    i += 1
print()

# Verificamos em qual índice um elemento está na tupla
# OBS: Caso o elemento não exista, será gerado um erro (ValueError)
# OBS2: Caso haja elemento repitido, ele retornará a primeira ocorrência do elemento
print(meses.index('Junho'))

# Slicing
# tupla[início,fim,passo]

print(meses[5::])
print(meses[5:9:])
print(meses[::])
print(meses[0::2])
print(meses[-3::-1])

# Por quê utilizar tuplas?

# tuplas são mais rápidas do que listas.
# tuplas deixam seu código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz mais segurança para o código

# Copiando uma tupla para outra
tupla = 1, 2, 3
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = 4, 5, 6
nova = nova + outra

print(nova)
print(tupla)
"""

