"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""

"""
Inicializando os variáveis maior e menor com o primeiro número da sequência

Depois um loop que roda 9 vezes
    Após isso é só comparar os valores anteriores com o atual lido e, se for maior ou menor, guardar nas variáveis
    corretas
    
Terminando isso é só printar
"""
menor = maior = float(input())
for n in range(9):
    numero = float(input())
    if numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
print(f'O maior número é {maior}'
      f'O menor número é {menor}')
