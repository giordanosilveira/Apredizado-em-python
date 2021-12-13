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
cores = ['verde', 'vermelho', 'amarelo', 'laranja', 'rosa']

# Utilizando uma função integrada (Built-in) do Python print ()
print(cores)

nome = 'Giordano Henrique Silveira'
print(nome)

cores.append('roxo')
print(cores)

# nome.append('Vai dar erro')  # AttributeError
# 'str' object has no attribute 'append'
# print(nome)

cores.clear()
print(cores)

print(help(print))
# Dry - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código
