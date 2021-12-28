"""
Enunciado:

Num print da pasta
"""

resposta_alunos = dict()

# Para cada aluno
for i in range(3):

    # lendo o seu número de matrícula
    aluno = int(input(f'Digite o número da matrícula do {i + 1}º aluno '))

    # Lendo suas respostas
    print(f'Digite as respostas do {i + 1}º aluno {aluno}', end=' ')
    respostas = []
    respostas = [input() for i in range(10)]

    # Adicionando os dados num dicionário, porque sim
    resposta_alunos[aluno] = respostas

print('Digite o gabarito das questões ')
# Lendo o gabarito das 10 questões
gabarito = []
for i in range(10):
    gabarito.append(input())

print(gabarito)

# Para cada aluno
for i in resposta_alunos:
    nota = 0

    # Para cada resposta do aluno
    for j in range(len(gabarito)):

        # Comparando suas respostas com o gabarito, caso acerte, a nota aumenta em um
        if resposta_alunos[i][j] == gabarito[j]:
            nota = nota + 1
    print(f'O aluno {i} tirou nota {nota}. Suas respostas foram {resposta_alunos[i]}')

