"""
Escopo de variáveis

Dois casos de escopo:

1  - Variáveis globais
    - Variáveis globais são reconhecidas, ou seja , seu escopo compreende todo o programa
2 - Variáveis locais
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja , seu escopo está limitado ao
    bloco onde foi declarada

Para declarar variáveis em python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de
dado dela. Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C
int c = 90;

"""

numero = 42
print(numero)
print(type(numero))

numero = 'Giba'
print(numero)
print(type(numero))

numero = 22
novo = 0

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)
