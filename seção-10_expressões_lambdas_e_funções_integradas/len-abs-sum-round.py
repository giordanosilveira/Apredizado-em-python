"""
len, abs, sum, round

# len
len() -> retorna o tamanho (ou seja, o número de itens) de um iterável.

# Revisando
print(len('Giordano Henrique Silveira'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len(range(0, 10)))

# Por baixo dos panos
# Dunder len
print('Giordano Henrique Silveira'.__len__())

#Abs
abs() -> retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o valor real sem o sinal.

# Exemplo
print(abs(-5))
print(abs(5))
print(abs(3.155))
print(abs(-3.155))

#Sum
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial
OBS: O valor inicial default é 0

# Exemplo
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([3.21, 4.213, 41.231]))
print(sum((1, 2, 3, 4, 5, 6)))

#Round
round() -> Retorna um número arredondado para n dígito de precisão após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo da entrada.

# Exemplos
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.231321231, 2))
print(round(1.219999999, 2))

"""


