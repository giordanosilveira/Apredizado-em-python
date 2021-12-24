"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!
OBS: A função do usuário é FODER o seu sistema.

# Else -> É executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Finally -> É executado sempre. Independentemente se houve exceção ou não
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Depois do bloco try/except')

# O finally, geralmente, é fechado para desalocar ou fechar recursos.

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a/b

num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser númerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo correto
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Divisão por 0'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

# Exemplo mais complexo - genérico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

# Exemplo mais complexo - Semi-Genérico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

"""

