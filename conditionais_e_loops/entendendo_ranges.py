"""
Ranges

- Precisamos entender o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada

Formais gerais:
range (valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)
#Forma 1
for num in range(11):
    print(num, end=' ')


OBS: valor_de_parada não inclusive (Início especificado pelo usuário, e passo de 1 em 1)
# Forma 2
range (valor_de_inicio, valor_de_parada)
for num in range(1, 11):
    print(num, end=' ')

OBS: valor_de_parada não inclusive
#Forma 3
range (valor_de_início, valor_de_parada, passo)
for num in range(0, 10, 2):
    print(num, end=' ')

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)
# Forma 4 (Forma 3 inversa )
range (valor_final(valor_de_início), valor_de_parada, passo)
for num in range(10, -1, -1):
    print(num)
    
"""
