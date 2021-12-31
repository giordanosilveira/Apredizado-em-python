"""
O bloco with

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo
2 - Trabalhar o arquivo
3 - Fechar o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos de trabalhos são fechados após o bloco with
arquivo = open('texto.txt')

"""

# O bloco with - Forma Pythônica de manipular arquivo
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)
    
# print(arquivo.read())
print(arquivo.closed)

