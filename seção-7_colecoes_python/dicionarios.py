"""
Dicionários

OBS:Em algumas linguagens de progrmação, os dicionários python são conhecidos por mapas.

Isso porque dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

Sobre dicionários:

    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados

#  Criação de dicionários

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguais'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1: Acessando via chave, acessando da mesma forma que lista/tupla
# OBS: Caso tentemos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError
print(paises['br'])
# print(paises['ru'])

# Forma 2: Acessando via get - Recomendado
# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError
print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru')
if pais:
    print(f'Encontrei o país {pais} ')
else:
    print('Não encontrei o país')

# Podemos definir uma valor padrão para caso não encontremos o objeto informado
pais = paises.get('py', 'Não encontrado')
print(f'Encontri o pais {pais}')

# Podemos verificar se determinada chave está no dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
# print(russia)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
#  podemos utilizar qualquer tipo de dado (int, float, string, boolean, lista, tupla, dicionário, como chaves de dicionários)

#  Tuplas por exemplo são bastantes interessante de serem utilizadas como chave de dicionários, pois essas são
#  imutáveis
localidades = {
    (35.6895, 39.67841): 'Escritório em Tóquio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 = Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão1: A forma de adicionar novo elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão2: Em dicionários NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

# Forma 1 - Mais comum
# OBS1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS2: Ao removermos um objeto, o valor deste objeto é sempre retornado
ret = receita.pop('mar')
print(ret)
print(receita)

# Forma 2
# OBS: Se a chave não existir será gerado um KeyError
# OBS2: Neste caso o valor removido não é retornado
del receita['fev']
print(receita)

# Imagine que você tem um comercio eletrônico, onde temos um carrinho de comprar na qual adicionamos produtos
Carrinho de compras:
    produto 1:
        - nome;
        - quantidade;
        - preço;
    produto 2:
        - nome;
        - quantidade;
        - preço;

# 1º - Poderiamos utilizar uma lista para isso? sim
# Teríamos que saber qual é o índice de cada informação no produto
carrinho = []
produto1 = ['play 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# 2º - Poderíamos utilizar uma tuplas para isso? sim
produto1 = ('play 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

# 3º - Poderíamos utilizar um dicionário para isso? Sim
# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre
# cada informação.
carrinho = []
produto1 = {'nome': 'Play 4', 'quantidade': '1', 'preco': '2300.00'}
produto2 = {'nome': 'God of War 4', 'quantidade': '1', 'preco': '150.00'}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Limpar o dicionário
d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1
# Deep copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(novo)
print(d)

# Forma 2
# Shallow copy
novo = d
print(novo)
novo['d'] = 4
print(novo)
print(d)

# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Forma não usual de criação de dicionários
# O método fromkeys recebe dois parâmetros: um interável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

veja = {}.fromkeys('teste', 'valor')
print(veja)
print(type(veja))

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""

