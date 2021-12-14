"""
Definindo Funções

- Funções são pequenos partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela; é bom fazer uma verificação para que a
função seja simplificada.

Já utilizamos várias funções desde que inicializamos este curso:
- print();
- len()
- max ()
- min ()
- count ()
- e muitas outras;
"""
# Exemplo de utilizações de funções
# cores = ['verde', 'vermelho', 'amarelo', 'laranja', 'rosa']

# Utilizando uma função integrada (Built-in) do Python print ()
#print(cores)

# nome = 'Giordano Henrique Silveira'
#print(nome)

# cores.append('roxo')
#print(cores)

# nome.append('Vai dar erro')  # AttributeError
# 'str' object has no attribute 'append'
# print(nome)

# cores.clear()
#print(cores)

#print(help(print))
# Dry - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

# Como definir funções

"""
Em python, a forma geral de definir uma função é:

def nome_da_função(parâmetros_da_entrada):
    bloco_da_função

Onde:
nome_da_função -> SEMPRE com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada são opcionais, onde tendo mais de um, cada um separado com ',' podendo ser opcionais ou não 
bloco_da_função -> também chamado de corpo da função, ou implementação, é onde o processamento da função acontece. Neste
bloco pode ter, ou não, retorno da função

OBS: Veja que para difinir uma função, utilizamos a palavra reservada 'def' informando ao python que estamos definindo
uma função. Também abrimos o bloco de código com o já conhecido ':' que é utilizado em Python para definir blocos
"""

# definindo a primeira função
def diz_oi():
    print('oi')

"""
OBS: 
1 - Veja que dentro das nossas funções, podemos utilizar outras funções:
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer 'oi'
3 - Veja que esta função não recebe nenhum parâmetro de entrada
4 - Veja que esta função não retorna nada 
"""

# Utilizando funções

"""
# Chamada de execução
# Atenção: nunca esqueça de utilizar o parênteses ao executar um função.
# Exemplo
# diz_oi -> Errado
# diz_oi() -> Certo
# diz_oi () -> Errado (fere a PEP8)
"""
# diz_oi()

# Exemplo 2
def cantar_parabens():
    parabens = """    
Parabéns para você 
Nesta data querida 
Muitas felicidades
Muitos anos de vida 
Viva o aniversariante"""
    print(parabens)


# for n in range (2):
#    cantar_parabens()

# Em python podemos inclusive criar variáveis do tipo de uma função e executar essa função atravéz da variável
cantar = cantar_parabens  # não é comum
cantar()

