from itertools import zip_longest
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
while (num1 > 10000 or num1 < 0) or (num2 > 10000 or num2) < 0:
    num1 = int(input('algum número não está entre 10000 e 0, digite um novo número: '))
    num2 = int(input('algum número não está entre 10000 e 0, digite um novo número: '))

num1 = [int(x) for x in str(num1)]
num2 = [int(x) for x in str(num2)]
num1.reverse()
num2.reverse()

lista_zip = list(zip_longest(num1, num2))

soma = []
vai_um = 0
for alg1, alg2 in lista_zip:
    if alg1 is None:
        if alg2 + vai_um >= 10:
            soma.append((alg2 + vai_um) % 10)
            vai_um = 1
        else:
            soma.append(alg2 + vai_um)
            vai_um = 0
    elif alg2 is None:
        if alg1 + vai_um >= 10:
            soma.append((alg1 + vai_um) % 10)
            vai_um = 1
        else:
            soma.append(alg1 + vai_um)
            vai_um = 0
    else:
        if alg2 + alg1 + vai_um >= 10:
            soma.append((alg2 + alg1 + vai_um) % 10)
            vai_um = 1
        else:
            soma.append(alg2 + alg1 + vai_um)
            vai_um = 0
if vai_um == 1:
    soma.append(1)

soma.reverse()
print(str(soma))


