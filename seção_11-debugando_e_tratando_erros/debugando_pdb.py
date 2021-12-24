"""
Debugando com PDB

PDB -> Python Debugger
VIDA DE INSETO -> Life's bug
BUG -> inseto

# OBS: A utilização do print() para debugar um código é uma prática ruim

def dividir(a, b):
    print(a, b)
    try:
        return int(a) / int(b)
    except: (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse debug, utilizando o debugger
# Em python, podemos fazer isso em diferentes IDE's, como o PyCharm ou utilizando o PDB

# PyCharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'

print(dividir(4, 7))

# PDB - Python Debugger - Exemplo 1
# Para utilizar o PDB, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Giordano Henrique'
sobrenome = 'Silveira'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Ciência da Computação'
final = nome_completo + ' faz o curso ' + curso
print(final)

# PDB - Python Debugger - Exemplo 2
# Para utilizar o PDB, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


nome = 'Giordano Henrique'
sobrenome = 'Silveira'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Ciência da Computação'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato ?
O debug é utilizado durante o desenvolvimento, por isso, ao invés de colocarmos o import do pdb no início do arquivo,
nós colocamos somente onde vamos debugar. Ao finalizar já fazemos a remoção da linha

# PDB - Python Debugger - Exemplo 3
# Para utilizar o PDB, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# A partir do python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como
# Função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


nome = 'Giordano Henrique'
sobrenome = 'Silveira'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Ciência da Computação'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com os conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, c, n, p):
    breakpoint()
    return l + c + n + p

print(soma(1, 3, 5, 7))

# Como os nomes das variáveis são os mesmos do comando do pdb, devemos utilizar o comando p para imprimir as variáveis
# Ou seja, p nome_da_variável

# Porém, nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.
# Exemplo
def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4

"""

