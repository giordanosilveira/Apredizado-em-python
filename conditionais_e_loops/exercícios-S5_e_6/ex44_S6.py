"""
Enunciado:

Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior ao
número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.
"""

n = int(input('Entre com um número positivo '))
soma = 1
anterior = 0
print(anterior, soma, end=' ')

# enquanto a soma não é maior que o n informado, continua no laço
while soma < n:
    aux = soma  # necessário para guardar o número anterior que é preciso para a sequência de fibonacci (soma do atual
    # com o anterior )
    soma = anterior + soma
    print(soma, end=' ')
    anterior = aux
