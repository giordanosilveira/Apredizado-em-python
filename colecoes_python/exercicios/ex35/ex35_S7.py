"""
Enunciado: Na imagem da pasta
"""

# Pedindo a entrada do usuário e, enquanto ele não digitar valores validos, pede para ele digitar novamente
num1 = int(input('Digite um número '))
num2 = int(input('Digite um segundo número '))
while num1 > 10_000 or num2 > 10_000:
    print('Alguns dos números ultrapassa o valor 10000 ')
    num1 = int(input('Digite um número '))
    num2 = int(input('Digite um segundo número '))

"""
Tudo isso é para transformar um inteiro em uma lista. Fiz isso para não mexer com MOD 10. Basicamente ele transforma o
inteiro em uma string, mapeia cada caractere da string em um int e transforma esse objeto mapeado em uma lista.

"""
num1 = str(num1)
num2 = str(num2)
num1 = map(int, num1)
num2 = map(int, num2)
num1 = list(num1)
num2 = list(num2)

# transforma as lista em um objeto tipo "zip". Usando o tipo zip você pode iterar duas ou mais coisas ao mesmo tempo
listas_juntas = zip(reversed(num1), reversed(num2))

resultado = list()
vai_um = 0  # vai_um variável que recebe um ou 0 conforme o resultado da soma

# Percorre as duas listas ao mesmo tempo
for i, j in listas_juntas:

    # Se a soma ultrapassar 10, guarda o último dígito no vetor e o vai_um = 1.
    if vai_um + i + j >= 10:
        resultado.append((vai_um + i + j) % 10)  # Mod 10 pega o último dígito
        vai_um = 1

    # Caso a soma seja menor, guarda o resultado dela no vetor
    elif vai_um + i + j < 10:
        resultado.append(vai_um + i + j)
        vai_um = 0

print(i, j)

# Caso sobre um ao final da soma, ele precisa ser contabilizado dentro do vetor
if vai_um == 1:
    resultado.append(vai_um)

# O Vetor está com resultado de trás para frente, visto que eu guardo os últimos algarismos nas primeiras posições.
# Então usamos a função reverse para ele ficar na ordem certa
resultado.reverse()
print(f'O resultado da soma é {resultado}')


