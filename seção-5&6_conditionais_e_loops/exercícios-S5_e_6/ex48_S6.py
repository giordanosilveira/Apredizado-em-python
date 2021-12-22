"""
Enunciado:

faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não ultrapassem quatro milhões
"""

soma = 1
soma_par = 0
anterior = 0
print(anterior, soma, end=' ')

# enquanto a soma não é maior que o n informado, continua no laço
while soma_par < 4_000_000:
    aux = soma  # necessário para guardar o número anterior que é preciso para a sequência de fibonacci (soma do atual
    # com o anterior )
    soma = anterior + soma
    if soma % 2 == 0:
        soma_par = soma_par + soma
    print(soma, end=' ')
    anterior = aux
print()
print(f'A soma dos pares da sequência de Fibonacci é {soma_par}')

