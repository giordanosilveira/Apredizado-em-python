"""
Enunciado:

Num print da pasta
"""

matriz1 = []
matriz2 = []

# List comprehension para inicializar a matriz1 com os valores passados pelo usuário
print('Digite os valores da matriz 1 ')
matriz1 = [[int(input()) for j in range(3)] for i in range(3)]

# List comprehension para inicializar a matriz2 com os valores passados pelo usuário
print('Digite os valores da matriz 2 ')
matriz2 = [[int(input()) for j in range(3)] for i in range(3)]

# Lista de opções para o usuário
print("Para somar duas matrizes digite 'add' ")
print("Para subtrair uma matriz da outra digite 'sub' ")
print("Para somar as matrizes com uma constante digite 'addc' ")
print("Para imprimir as duas matrizes digite 'imp' ")
print("Para multiplicar as duas matrizes digite 'mult' ")
opcao = input('Digite uma opção ')

# Se ele pediu soma
if opcao == "add":
    matriz3 = []

    # Para cada coluna da linha
    for k in range(3):
        soma = []

        # zipa os objetos para ficar mais fácil a interação, soma os valores da matrizes e coloca ele na lista 'soma'
        for i, j in zip(matriz1[k], matriz2[k]):
            soma.append(i + j)

        # Coloca o resultado de 'soma' na matriz 3
        matriz3.append(soma)
    print(f'A matriz resultado é {matriz3}')

# Se ele pediu para subtrair uma matriz da outra
if opcao == "sub":

    # Pergunta se ele quer subtrair a matriz 1 da 2 ou vice-versa
    ordem = input("'1' para subtrair a matriz 1 da matriz 2 e '2' para subtrair a matriz 2 da matriz 1 " )

    # subtrair matriz 2 da 1
    if ordem == 1:
        matriz3 = []
        for k in range(3):
            soma = []
            for i, j in zip(matriz1[k], matriz2[k]):
                soma.append(i - j)
            matriz3.append(soma)
        print(f'A matriz resultado é {matriz3}')
    else:
        matriz3 = []
        for k in range(3):
            soma = []
            for i, j in zip(matriz1[k], matriz2[k]):
                soma.append(j - i)
            matriz3.append(soma)
        print(f'A matriz resultado é {matriz3}')

# Se ele pediu para somar com constante
if opcao == "addc":

    # Pede para o usuário digitar o valor da constante
    const = float(input('Digite o valor da constante '))

    matriz3 = []
    matriz4 = []

    # Para cada coluna da linha
    for k in range(3):
        soma1 = []
        soma2 = []

        # zipa os objetos para ficar mais fácil a interação, soma os valores da matrizes com a constante
        # e coloca ele nas listas "soma's"
        for i, j in zip(matriz1[k], matriz2[k]):
            soma1.append(i + const)
            soma2.append(j + const)

        # Coloca o resultado de "soma's" na matriz 3 e 4
        matriz3.append(soma1)
        matriz4.append(soma2)

    print(f'A matriz1 ficou assim {matriz3}')
    print(f'A matriz2 ficou assim {matriz4}')

if opcao == "imp":
    print(f'A matriz1 é {matriz1}')
    print(f'A matriz2 é {matriz2}')

if opcao == "mult":
    mult = []
    for i in range(3):
        linha = []
        for j in range(3):
            soma = 0
            for k in range(3):
                soma = soma + matriz1[i][k]*matriz2[k][j]
            linha.append(soma)
        mult.append(linha)
    print(f'A matriz resultado é {mult}')