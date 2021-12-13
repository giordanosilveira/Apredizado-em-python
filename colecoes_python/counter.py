"""
Módulo Collections - Counter (contador)

Collections - High-Performance Container DateTypes

Counter -> Recebe um iteravel como parãmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo um como chave o elemento da lista passado como parâmetro e como valor a quantidade de ocorrências
desse elemento.

# Utilizando o counter

# Realizando o import
from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 3, 2, 3, 2, 1, 1, 1, 3, 4, 2, 1, 2, 4, 3, 5, 4, 4, 55, 4, 32, 3245, 51]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2
print(Counter('Giordano Henrique Silveira'))

# Exemplo 3
texto = Crazy Jane é uma personagem criada por Grant Morrison e Richard Case para sua versão da Patrulha do Destino
na Vertigo Comics. Ela aparece pela primeira vez em Doom Patrol Volume 2 #19 (Fevereiro de 1989).
De acordo com o posfácio da primeira coleção comercial em brochura da Patrulha do Destino de Morrison, ela é baseada em
Truddi Chase. Morrison estava lendo sua autobiografia, "When Rabbit Howls",  enquanto construía sua história da
Patrulha do Destino.

palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)

# Encontrando as cincos palavras com mais ocorrências no texto
print(res.most_common(5))

"""
# Realizando o import
from collections import Counter


