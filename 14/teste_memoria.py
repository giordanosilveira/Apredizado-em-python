"""
Testa de Memória com Generators


# teste 471MB - Usando lista
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

for n in fib_lista(100_000):
    print(n)
"""

# Função usando geradores
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1
        
# Teste 3,9MB - 4,1MB
for n in fib_gen(100_000):
    print(n)
