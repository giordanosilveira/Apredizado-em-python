"""
Funções com parâmetros Padrão (Default parâmetros)

- Funções onde a passagem de parâmetros seja opcional

# Exemplo de função com parâmetro opcional
print('Giordano Henrique Silveira')
print()

# Exemplo de função que a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

numero = 2
print(quadrado(numero))
print(quadrado())  # TypeError

# OBS: Se o usuário passar somente um parâmetro, este será atribuído ao parâmetro número, e será calculado o quadrado
# deste número
# Se o usuário passado dois argumento, o primeiro será atribuído ao parâmetro número e ao segundo ao parâmetro potencia.
# Então será calculada a esta potencia

def exponecial(numero=2, potencia=2):
    return numero ** potencia


print(exponecial(2, 3))  # == 8
print(exponecial(3, 2))  # == 9

print(exponecial(3))  # Por padrão, eleva ao quadrado
print(exponecial(3, 5))  # Eleva à potencia informada pelo usuário

print(exponecial())

# OBS: Em funções python, as funções com valores padrão (default) DEVEM sempre estar ao final da declaração

# Erro!
def teste(potencia, num=2):
    return num ** potencia


print(teste(6))

# Outro exemplos

def soma(num1=1, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   # TypeError

# Mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return f'Bem vindo instrutor {nome}'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao(('Ozzy')))

# Por quê utilizar parâmetros com valor Default?
# - nos permite ser mais flexíveis nas funções
# - Evita erros com parâmetro incorretos/
# - Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores Default para parâmtros ?
# - QUALQUER tipo de dados, inclusive até funções


# Exemplos

def soma(a, b):
    return a + b

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 3, subtracao))

# Escopo - Evitar probelemas e confusões...

# Variáveis Globais
# Variáveis Locais

instrutor = 'Geek'  # Variável global

# OBS: Se tivermos uma variável local e uma global com o mesmo nome, a local tera preferência
def diz_oi():
    instrutor = 'Python'  #  Variável local
    return f'Oi {instrutor}'

print(diz_oi())

def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'


print(diz_oi())
print(prof)  # NameError

total = 0
def incrementa():
    total = total + 1  # UnboundLocalError -> a variável local está sendo utilizada para processamento sem ter sido
                       # inicializada
    return total

print(incrementa())

# Atenção com variáveis globais (Se puder evitar, evite!)
total = 0
def incrementa():
    global total  # avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador

    return dentro()

print(fora())
print(fora())
print(fora())
print(dentro())  # NameError
"""
