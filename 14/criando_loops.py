"""
Criando sua própria versão de Loop

for num in [1, 2, 3, 4, 5, 6]:
    print(num)
    
for letra in "Giordano Henrique Silveira":
    print(letra)
    
iter([1, 2, 3, 4, 5, 6])
iter('Giordano Henrique Silveira')


"""

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for("Giordano Henrique Silveira")
numeros = [1, 2, 3, 4, 5, 6]
meu_for(numeros)

