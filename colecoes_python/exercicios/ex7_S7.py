"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. imprima o vetor, o menor e o maior elemento
e a posição que ele se encontra
"""
# Declarando um vetor vazio e preenchendo ele com os valores da entrada
vetor = []
print('Digite 10 números')
for i in range(10):
    vetor.append(int(input()))

# Procura o máximo e o mínimo dentro do vetor
maior = max(vetor)
menor = min(vetor)

# Procura esse valores dentro do vetor e guarda a posição deles em outra variáveis
for i in range(10):
    if maior == vetor[i]:
        pos_maior = i
    if menor == vetor[i]:
        pos_menor = i
print(f'O vetor é {vetor}')
print(f'O maior número da lista é {maior} e se encontra na posição {pos_maior} do vetor')
print(f'O maior número da lista é {menor} e se encontra na posição {pos_menor} do vetor')
