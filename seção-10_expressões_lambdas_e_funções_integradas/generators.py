"""
Generators Expression

Em aulas anteriores nós estudamos:
- list comprehension;
- Dictionary comprehension;
- Set comprehension;

Não vimos:
- Tuple comprehension porque eles se chamar Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# Poderiamos ter feitos utilizando Generators
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(res)
print(type(res))

# Mostra quantos bytes a string 'Geek' está ocupando na memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('geek'))
print(getsizeof('Giordano'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(84718972481))
print(getsizeof(True))

# Qual é a utilizadade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Gerando uma lista de números como List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números como Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números como Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números como Generator
gen = getsizeof(x * 10 for x in range(1000))

print(f'Tamanho em bytes do list: {list_comp}')
print(f'Tamanho em bytes do set: {set_comp}')
print(f'Tamanho em bytes do dic: {dic_comp}')
print(f'Tamanho em bytes do gen: {gen}')

# Eu posso iterar no Generator Expression ? sim
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
"""
