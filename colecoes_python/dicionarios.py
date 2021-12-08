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
 """
# Adicionar elementos em um dicionário

# Atualizando dados em um dicionário