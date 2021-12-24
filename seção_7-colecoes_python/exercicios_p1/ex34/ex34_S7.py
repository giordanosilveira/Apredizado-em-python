"""
Enunciado: Na imagem que está junto a pasta
"""

# Gerando uma lista vazia e depois inicializando ela com a primeira entrada do usuário
numeros = list()
numeros.append(int(input('Digite 10 números diferentes\n')))

# Começa de 1 porque já foi o primeiro elemento
i = 1

# Enquanto não deu 10 elementos, permanece no loop
while i < 9:

    # Nova entrada
    num = int(input())

    # Se tiver um número igual no vetor, não faz nada. Apenas printa a mensagem.
    if num in numeros:
        print('Número repitido. Digite outro número')

    # Caso não tenha, coloca ela no vetor e incrementa a variável que controla o tamanho do vetor
    else:
        numeros.append(num)
        i += 1

print(f'lista de números {numeros}')

