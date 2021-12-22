"""
Entendendo o *args

O * args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que
começe com '*'

Exemplo:
*xis

Mas por conversão, utilizamos o *args para definí-lo
Mas o que é o *args ?

O parâmentro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis


def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(4, 6, 9, 5))

# Entendendo o *args
def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Giordano ', ' Henrique'))
print(soma_todos_numeros('Giordano ', ' Henrique', 1))
print(soma_todos_numeros('Giordano ', ' Henrique', 1, 2))
print(soma_todos_numeros('Giordano ', ' Henrique', 2, 3, 4))
print(soma_todos_numeros('Giordano ', ' Henrique', 23.4, 12.5))

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Quem é você ?'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.14))


"""

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 23, 4))

numeros = {1, 2, 3, 4, 5, 6}

# Desempacotador
# O * serve que para informamos ao Python que estamos passando como argumento uma coleção de dados. Desta forma
# ele saberá que precisará antes desempacotar esses dados.
# print(soma_todos_numeros(numeros))  # TypeError
print(soma_todos_numeros(*numeros))
