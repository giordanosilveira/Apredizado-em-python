"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da matemática.

- aqui no Python os conjuntos são chamados de Sets.

Dito isso, da mesma forma da matemática:

    - Sets (conjuntos) não possuem valores duplicados:
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessdos via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferenças entre Conjuntos (Set) e Mapas (dicionários) em Python:

    - Um dicionário tem {chave: valor};
    - Um Conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não
# fará parte do conjunto
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(s)
print(type(s))

# Forma 2 - mais comum
s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print(s)
print(type(s))

# Podemos verificar se um determina elemento está contido num conjunto
n = 13
if n in s:
    print(f'Tem o valor {n}')
else:
    print(f'Não tem o valor {n}')

# Importante lembrar que além de não termos valores duplicados, não temos ordem

# listas aceitam valores duplicados
lista = [99, 12, 3, 5, 23, 5, 1, 0, 12, 34]
print(f'lista: {lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados
tupla = (99, 12, 3, 5, 23, 5, 1, 0, 12, 34)
print(f'tupla: {tupla} com {len(tupla)} elementos')

# dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys(lista, 'dict')
print(f'dicionário: {dicionario} com {len(dicionario)} elementos')
print(type(dicionario))

# Conjuntos não aceitam valores duplicados
s = {99, 12, 3, 5, 23, 5, 1, 0, 12, 34}
print(f's: {s} com {len(s)} elementos')

# Assim como todo outro conjunto Python, podemos colocar tipo de dados misturados em Sets
s = {1, 'b', True, 34.22, 4}
print(s)
print(type(s))

# Podemos Iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam manualmente
# a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista python, já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, única temos.
# Podemos utilizar um set para isso

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
print(s)
s.add(4)
s.add(4)  #  Duplicidade não gera erro, somente é ignorado
print(s)

# Removendo elementos em um conjunto

# Forma 1
# OBS: Caso o valor não seja encontrado, será gerado o erro KeyError
# OBS 2: Nenhum valor é retornado
s = {1, 2, 3}
print(s)
s.remove(3)  # Valor a ser removido
print(ret)
print(s)

# Forma 2
# OBS: Se o valor não for encontrado, nenhum erro é gerado
# OBS 2: Nenhum valor é retornado
s.discard(22)
print(s)

# Copiando um conjunto para outro

s = {1, 2, 3}
print(s)

# Forma 1: Deep copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 2: Shallow copy
novo = s
print(novo)
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s = {1, 2, 3}
print(s)
s.clear()
print(s)

# Métodos matemáticos de conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes de curso Python e um contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patrícia', 'Felipe', 'João', 'Pedro', 'Júlia'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}

# Veja que alguns alunos que estamos estudam Python e também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1: Utilizando union
# Tanto faz a ordem
estudantes = estudantes_python.union(estudantes_java)
print(estudantes)

# Forma 2: Utilizando o caractere pipe '|'
estudantes2 = estudantes_python | estudantes_java
print(estudantes2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1: Utilizando o intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2: Utilizando o caractere '&'
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, valor maximo*, valor mínimo*, quantidade
# * Funciona quando todos os valores são inteiros e/ou reais
s = set(range(12))
print(s)

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""
