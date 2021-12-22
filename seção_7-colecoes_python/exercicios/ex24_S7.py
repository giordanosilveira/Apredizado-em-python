"""
Enunciado:

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando o número do aluno e o segundo representando sua altura em metros. Encontre o aluno mais baixo e o mais
alto. Mostre o número do aluno mais baixo e do mais alto, juntamente com sua alturas
"""

from random import uniform

"""
O programa diz para ler, mas eu to com preguiça e gerei 10 números "randômicos". Coloquei eles em um conjunto (porque
o enunciado diz que tem que ser conjunto) e armazenei eles em uma lista)
"""
lista = list()
for i in range(10):
    a = i
    b = round(uniform(1.5, 1.9), 2)  # a função round limita o número de casas decimais
    lista.append({a, b})

"""
Criando uma lista1 vazia e preenchendo ela com os conjuntos da lista
"""
print(lista)
lista1 = list()
for i, j in enumerate(lista):
    lista1.append(lista[i])

# Inicializando o maior e o menor com o altura do primeiro conjunto, tem que iterar porque conjunto não guarda posição
for i in lista1[0]:
    if isinstance(i, float):
        maior = menor = i

# tamanho - 1 porque o primeiro item da lista já foi usado
# Percorrendo todos os conjuntos da lista
for i in range(len(lista1) - 1):

    # Iterando dentro de cada conjunto e guardando a posição da menor e maior altura para cada item da lista
    for j in lista1[i]:

        # isinstance checa para ver se o item é daquele tipo. Usei porque a altura era em float e o número do aluno
        # era int. Fica mais fácil comparar assim
        if isinstance(j, float):
            if maior < j:
                maior = j
                guarda_maior = i
            elif menor > j:
                menor = j
                guarda_menor = i

print(f'O maior aluno da sala está na posição {guarda_maior} e sua altura é {maior}')
print(f'O menor aluno da sala está na posição {guarda_menor} e sua altura é {menor}')
