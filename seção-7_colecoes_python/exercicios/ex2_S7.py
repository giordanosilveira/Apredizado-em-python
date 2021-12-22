"""
Enunciado:

Ler um conjunto de números reais, armazenando-o em um vetor e calcular o quadrado dos componentes deste vetor,
armazenando o resultado em outro vetor. Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos
"""

# Declarando os dois vetores
vetor_reais = []
quadrado_reais = []

print('Digite somente números reais')
# Laço que roda 10 vezes porque os vetores tem que ter 10 elementos
for i in range(10):
    vetor_reais.append(float(input()))  # Adiciona no vetor o input do usuário

    # No mesmo laço calcula o quadrado desse número e coloca na posição certa
    quadrado_reais.append(vetor_reais[i]*vetor_reais[i])
print(vetor_reais)
print(quadrado_reais)
