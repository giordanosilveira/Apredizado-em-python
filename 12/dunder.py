"""
Dunder Name e Dunder main

Dunder -> double Under

Dunder name -> __name__
Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc, utilizando Double Under para não ferar conflito com os nomes desses elementos
na programação.

# Em C, temos um programa da seguinte forma:
int main (){
    return 0;
}

public static void main (String[], args) {
    
}

# Em python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variável __name__ o valor __main__ indicando que este
módulo é o módulo de execução principal

#Importando o módulo do diretório pai
import sys
sys.path.insert(1, '../')

from funcoes_com_parâmetro import soma_impares as si
print(si([1, 2, 3, 4, 5, 6, 7]))

# OBS: VER OS ARQUIVOS PRIMEIRO.PY e SEGUNDO.PY
"""
import primeiro
import segundo

