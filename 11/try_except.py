"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare
de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:
try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas

# Exemplo 1 - Tratando um erro genérico
# Tente executar a função geek, caso encontre erros, imprima a mensagem de erro
try:
    geek()
except:
    print('Deu ruim José')

# Exemplo 2
try:
    len(5)
except:
    print('Deu ruim José')

OBS: Tratar o erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar o erro de
forma específica

# Exemplo 3 - Tratando um erro específico
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico
try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez
try:
    # len(5)
    print('geek'[32])
except NameError as err:
    print(f'Deu NameError {err}')
except ValueError as err2:
    print(f'Deu ValurError {err2}')
except TypeError as err3:
    print(f'Deu TypeError {err3}')
except:
    print('Deu um erro diferente')


"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "giba"}
print(pega_valor(dic, "nome"))
