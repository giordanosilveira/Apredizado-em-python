"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO e também
de podermos colocar QUALQUER tipo de dado.

Linguagem C/JAVA: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro
    e poderá ter SEMPRE no máximo 5 valores

Já em Python:

- Dinâmico: Não possuem tamanho fixo. Ou seja, podemos criar a lista e simplemente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo. Ou seja, podemos criar qualquer tipo de dado;

As listas em Python são representadas por colchetes []
As listas são mutáveis

type([])
lista1 = [1, 2, 99, 4, 217, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'i', 'o', 'r', 'd', 'a', 'n', 'o', ' ', 'S', 'i', 'l', 'v', 'e', 'i', 'r', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('Giordano Silveira')

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'O número {num} está aqui')
else
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos na lista:

    # Para adicionar elementos em listas, utilizamos a função append
    print(lista1)
    lista1.append(42)
    print(lista1)
    #OBS: Com append, nós só podemos adicionar 1 elementos por vez
    lista1.append(12, 34, 56) -> Erro

    lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)
    print(lista1)

    if [8, 3, 1] in lista1:
        print('Encontrei a lista')
    else:
        print ('Não encontrei a lista')

    # extend: Coloca cada elementos da lista como valor adicional à lista
    lista1.extend([23, 44, 67])
    print (lista1)

#  POdemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita
lista1.insert(2, 'Novo Valor')
print(lista1)

#  Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

#  Podemos facilmente reverter uma lista

    #  Forma 1
    lista1.reverse()
    lista2.reverse()

    print(lista1)
    print(lista2)

    #  Forma 2:
    print(lista1[::-1])
    print(lista2[::-1])

#  Podemos copiar uma lista
lista6 = lista1.copy()
print(lista6)

#  Podemos contar quantos elementos existem dentro da lista
print(len(lista5))

#  Podemos remover facilmente o último elemento da lista
#  OBS: o pop não só remove o último elemento como também o retorna
print(lista2)
lista2.pop()
print(lista2)

# podemos remover um elemento pelo índice
# OBS: Os elementos á direita deste índice serão deslocados para à esquerda
# OBS2: Se bão houver elemento no índice informado, teremos o índice IndexError
print(lista2)
lista2.pop(7)
print(lista2)

# Podemos remover todos os elementos da lista
print(lista5)
lista5.clear()
print(lista5)

#  Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#  Podemos facilmente converter uma string para uma lista
    #  Exemplo 1:

    curso = 'Giordano Henrique Silveira'
    print(curso)
    curso = curso.split()
    print(curso)

    #  OBS: Por padrão, o split separa os elementos lista pelo espaço entre elas.

    #Exemplo 2
    curso = 'Giordano,Henrique,Silveira'
    print(curso)
    curso = curso.split(',')
    print(curso)

# Convertendo uma lista em uma string
# Coloca espaços entre os elementos e transforma em uma String

curso = ' '.join(curso)
print(curso)

lista6 = [1, 2.34, True, 'Giordano', 'd', [1, 2, 3], 65312653]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando o for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando o while

carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#  Fazemos acesso aos elementos de forma indexada
#           0         1         2       3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
#  Vetores em Python funcionam de forma circular
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # Erro, não existe indice -5

cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# listas ACEITAM valores repetidos

# Outros métodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
# OBS2: Em caso de repetição, o index retornará o primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar e também qual parar
print(numeros.index(5, 1))  # buscando 5 a partir do índice 1
print(numeros.index(5, 4, 7)) # Buscando o 5 a partir do indice 4 e parando no 7

# Revisão de slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de listas com o parâmetro 'início'
lista = [1, 2, 3, 4]
print(lista[1::]) # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de listas com o parâmetro 'fim'
lista = [1, 2, 3, 4]
print(lista[:2:])
print(lista[1:3:])

# Trabalhando com slice de listas com o parâmetro 'passo'
lista = [1, 2, 3, 4]
print(lista[::2])

# Invertendo valores em uma lista
nome = ['Giordano', 'Silveira']
print(nome)
nome[0], nome[1] = nome[1], nome[0]
print(nome)

nome = ['Giordano', 'Silveira']
print(nome)
nome.reverse()
print(nome)

# Soma* , Valor máximo, Valor mínimo, tamanho
# * valores inteiros, ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma lista, mas elas ficaram totalmente
# independentes, ou seja, modificando uma lista, não afeta a outra. Isso em python é chamado de Deep Copy (Cópia profunda)

# Forma 2
lista = [1, 2, 3]
print(lista)
nova = lista

print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu am ambas as listas. Isso em Python
# é chamando de Shallow Copy
"""

