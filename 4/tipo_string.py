"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
- Estiver entre aspas duplas triplas

nome = "Giordano's bar \nHenrique Silveira"
print(nome)
print(type(nome))

print(nome.split()) -> transforma em uma lista de strings

# [ 0,   1,   2,   ...                  7]
# ['G', 'i', 'o', 'r', 'd', 'a', 'n', 'o', ...]
nome = 'Giordano Henrique Silveira'
print(nome[0:8]) #slice de string

print(nome[18:26])

print(nome.split()[0])

print(nome.split()[1])

print(nome.split()[2])

"""
# nome = """Angelina
# Jolie"""
# print(nome)
# print(type(nome))

# [ 0,   1,   2,   ...                  7, ...]
# ['G', 'i', 'o', 'r', 'd', 'a', 'n', 'o', ...]
nome = 'Giordano Henrique Silveira'

print(nome[::-1])  # Comece do primeiro elemento, vá até o último elemento e invertat

print(nome.replace('a', 'k'))
