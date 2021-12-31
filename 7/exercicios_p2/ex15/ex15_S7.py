"""
Enunciado:

Num print da pasta
"""

import random

# Escolhas possíveis de respostas das questões
escolhas = ['a', 'b', 'c', 'd', 'e']

# inicializa o vetor gabarito com uma resposta para cada questão
gabarito = [random.choice(escolhas) for i in range(10)]
print('O gabarito')
print(gabarito)

alunos = []
resultado_aluno = []
# Para cada aluno

for j in range(5):

    # Suas respostas
    respostas = []
    for i in range(10):
        respostas.append(random.choice(escolhas))
    print(respostas)
    alunos.append(respostas)


# Para cada aluno
for i in range(5):

    # Para cada resposta do aluno
    nota = 0
    for j in range(10):

        # Compara o gabarito com as resposta do aluno e, a cada acerto, a nota aumeta um ponto
        if gabarito[j] == alunos[i][j]:
            nota += 1

    resultado_aluno.append(nota) # Coloca o resultado na lista notas

# Printa o resultado
for i, nota, in enumerate(resultado_aluno):
    print(f'O aluno {i} tirou {nota} na prova')
