"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;
Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado para manter compatibilidade


# importando todo o pacote
from exemplo import ex1, ex2
from exemplo.sub_exemplo import ex3, ex4

# Usando o pacote
print(ex1.pi)
print(ex1.função1(4, 6))
print(ex2.nome)
print(ex2.funcao2())
print(ex3.funcao3())
print(ex4.funcao4())



"""

from exemplo.ex1 import função1 as f
from exemplo.sub_exemplo.ex4 import funcao4 as f4
print(f(6, 9))
print(f4())


