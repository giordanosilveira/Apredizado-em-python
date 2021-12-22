"""
Módulo Collections - Default Dict

# Recap dicionários
dicionario = {'nome': 'Giordano Henrique Silveira'}
print(dicionario)
print(dicionario['nome'])

print(dicionario['outro']) # KeyError

Default Dict -> ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda para
isso. Esse valor será utilizado SEMPRE que não houver um valor definido. Caso tentemos acessar uma chave inexistente,
essa chave será criada e o valor default será atribuído

OBS: lambdas são funções sem nome, que podem, ou não, receber parâmetros de entrada e retornar valores.

from collections import defaultdict
dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['nome'] = 'Giordano Henrique Silveira'
print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum
print(dicionario)
"""

