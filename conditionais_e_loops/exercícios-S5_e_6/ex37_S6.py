"""
Enunciado:

Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma dos
dois dígitos de mais baixa ordem com os dígitos de mais alta ordem elevada ao quadrado é igual ao próprio número. Por
exemplo, para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025

"""

# Percorre entre os valores pedidos
for i in range(1000, 9999 + 1):
    div = 100   # Div 100 para separar as duas metades do número
    num1 = i % div  # (1234 % 100 = 34)
    num2 = int(i/div)   # (1234/100 = 23)
    soma = num1 + num2
    if soma * soma == i:
        print(f'A soma de num1 + num2 = {soma}. O quadrado de {soma} é igual a {soma*soma} que por sua vez '
              f'é igual a {i}')
