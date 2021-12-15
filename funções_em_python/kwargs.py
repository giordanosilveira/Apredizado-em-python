"""
**kwargs

Poderiamos chamar esse parâmetro de **xis, mas por convenção chamamos de **kwargs

Este só é mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla. O **kwargs exige que
utilizemos parâmetro nomeados, e trasforma esses parâmetros extras em um dicionário

# Exemplo 1
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='rosa', fernanda='azul', vanessa='branco')

# OBS: nem os parâmetro *args e **kwargs não são obrigatórios
cores_favoritas()
cores_favoritas(marcos='rosa')

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'Geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é '

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossão funções podemos ter (NESTA ORDEM):
# - Parâmetro obrigatórios
# - *args
# - Parâmetros default (não obrigatórios);
# - **kwargs

def minha_funcao(num, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {num} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

minha_funcao(22, 'Giordano')
minha_funcao(22, 'Jessica', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Pedro', eu='Não', voce='vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, Python=True)

# Entenda porquê é importante manter a ordem dos parâmetros na declaração
# Função com a ordem correta de parâmetros

a=1. b=1, args = 3, instrutor='Geek', kwargs={'sobrenome':'University', 'cargo':'instrutor)

# def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

#Função com a ordem incorreta de parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))

# Desempacotar com **kwargs
def mostra_nomes(**kwags):
    return f"{kwags['nome']} {kwags['sobrenome']}"

nomes = {'nome': 'Giordano', 'sobrenome': 'Silveira'}
print(mostra_nomes(nome='Giordano', sobrenome='Silveira'))
print(mostra_nomes(**nomes))

def soma_multiplos_numeros (a, b, c, **kwargs):
    print(a + b + c)

soma_multiplos_numeros(1, 2, 3)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

#OBS! Os nomes das chaves de um dicionário devem ser o mesmo dos parâmetros da função
#dicionario = dict(d=1, e=2, f=3)  # TypeError
#soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Giba')
soma_multiplos_numeros(**dicionario, apelido='Giba')
"""
