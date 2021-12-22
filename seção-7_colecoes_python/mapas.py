"""
Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

# Iterar sobre dicionários
for chave in receita:
    print(chave, end=' ')
print()

for chave in receita:
    print(receita[chave], end=' ')
print()

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

# Acessando as chaves
print(receita.keys())
for chave in receita.keys():
    print(receita[chave])


# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor, end=' ')
print()

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}', end=' ')

# Soma*, valor_maximo*, valor_minimo*, tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
