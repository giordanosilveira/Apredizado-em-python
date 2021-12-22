"""
Erros mais comuns em python

IMPORTANTE: LEIA A PORRA DO ERRO!

Os erros mais comuns:

SyntaxError -> Ocorre quando o python encontra um erro de síntaxe. Ou seja, você escreveu algo que o python não
reconhece como parte da linguagem

# Exemplos
# falta o () depois da função
def funcao:
    return 'Erro'

# Usando palavra reservada
None = 1
def = 1

# Deve ser usado dentro de uma função
return

NameError -> Ocorre quando uma variável ou uma função não foi definida.
# Exemplos

# Imprimindo uma variável que não existe
print(geek)

# Aplicando uma função não definida
geek()

# Utilizando variável que foi criada localmente
a = 18
if a < 10
    msg = 'Vai Corinthians'
print(msg)

TypeError -> Ocorre quando uma função/operação/ação é aplicada sobre um tipo errado
# Exemplos

#Passando um int que não tem tamanho para a função len()
print(len(5))

#Tentado concatenar uma string com uma lista vazia
print('abc' + [])

IndexError -> Ocorre quando acessamos uma posição inexistente em um iterável indexado (lista, tupla)
# Exemplos

# A lista tem tamnho 1 e você tentou acessar o elemento 2
dados = ['giba']
print(dados[2])

# A string tem 4 elementos e você tentou acessar o elemento 23
dados = ['giba']
print(dados[0][23])

ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor
inapropriado
# Exemplos

# O int() pode transformar uma string para um int, mas o valor passado está errado
print(int('giba'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe
# Exemplos

# O dicionário está vazio e você está tentando acessar ele com uma chave que não existe
d = {}
print(d['geek'])

AttributeError -> Ocorre quando uma variável não tem um atributo/função
# Exemplos

# Fazendo uma função que não existe para o tipo de dado tupla
tupla = 1, 2, 3, 4
tupla.sort()

IdentationError -> Ocorre quando não respeitamos a identação do python (4 espaços)
# Exemplos

def nova():
print('giba')

for i in range(10):
i + 1

OBS: Exceptions e Erros são sinônimos na programação
OBS: LEIA A PORRA DOS ERROS NA SAÍDA
"""



