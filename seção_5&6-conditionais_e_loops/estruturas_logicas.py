"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not' o valor do booleano é invertido, ou seja, se for True, vira False e vice-versa
"""
ativo = False
logado = False

if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por Favor, cheque seu e-mail')

# Se não estiver ativo
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print(not False)
print(not True)

if ativo is True:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por Favor, cheque seu e-mail')

# ativo é True?
    print(ativo is True)
