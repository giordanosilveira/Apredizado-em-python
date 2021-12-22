"""
Enunciado:

Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número
foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

"""
qtd recebe da entrada padrão quantos números vão ser lidos

maior é inicializado com o primeiro valor da sequência informada pelo usuário

o loop roda qtd - 1 vezes:
    Se o número atual for maior que o número guardado maior recebe número
    e o conta_maior é definido para 1 visto que apareceu pelo menos 1 vez
    
Ao sair do loop o maior número e a quantidade de vezes que ele apareceu é printada.
"""

qtd = int(input('Quantos números vão ser lidos '))
maior = float(input('Digite os números\n'))
conta_maior = 1
for n in range(qtd - 1):
    conta_maior += 1
    numero = float(input())
    if numero > maior:
        maior = numero
        conta_maior = 1
print(f'O maior número da sequência de {qtd} números for: {maior} e ele apareceu {conta_maior} vezes')
