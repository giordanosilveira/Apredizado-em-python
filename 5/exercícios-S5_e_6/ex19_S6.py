"""
Enunciado:

Escreva um algotimo que leia um número inteiro entre 100 e 999 e imprima cada um dos algarismos que compõem o número
"""

div = 100
n = int(input('Escreva um número entre 100 e 999 '))
# Caso o usuário entre com algum valor inválido
if n > 999 or n < 100:
    print(f'O número {n} é inválido')
else:  # Se está tudo certo
    # Divide por 100 porque são 3 algarismos (se fosse 4 algarismos dividiria por 1000)
    # a cada volta do laço div vai sendo dividido por 10, porque o número de algarismos no número 'n' diminui
    while div >= 10:
        print(int(n/div), end=' ')  # 123/100 = 1; 123 % 100 = 23
        n = n % div;
        div /= 10
    print(int(n))  # Printa o último dígito

