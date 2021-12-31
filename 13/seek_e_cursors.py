"""
Seek e Cursors

seek() -> é utilizado para movimentar o cursor pelo arquivo
arquivo = open('texto.txt')
print(arquivo.read())

# A seek() -> a função seek() é utilizada para a movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar o cursor 
# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(22)
print(arquivo.read())

# readline() -> Função que lê o arquivo linha a linha
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))

# readlines() -> converte cada linha de um texto para um item de uma lista
linhas = arquivo.readlines()
print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o nosso programa. Essa conexão é chamada de
streaming. Ao finalizar os trabalho com o arquivo devemos fechar essa conexão. para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo
2 - Trabalhar o arquivo
3 - Fechar o arquivo

# 1 - Abrir o arquivo
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo
print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
"""

arquivo = open('texto.txt')

# lendo um limitando o número de caracteres
print(arquivo.read(30))
