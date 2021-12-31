"""
Enunciado:

Num print da pasta
"""
from random import randint

notas_alunos = []
# Item a)
# Para cada aluno
for i in range(5):

    informacoes = []
    informacoes.append(int(input(f'Digite o número de matrícula do {i + 1}º aluno ')))

    prova_nota = []
    # Gera as notas das provas dele (gerando fica mais fácil para testar)
    for k in range(3):
        prova_nota.append(randint(0, 10))
    informacoes.append(prova_nota)

    trabalho_nota = []
    # Gera as notas dos trabalhos dele (gerando fica mais fácil para testar)
    for k in range(3):
        trabalho_nota.append(randint(0, 10))
    informacoes.append(trabalho_nota)

    # Colocando essas informações no vetor
    notas_alunos.append(informacoes)

print(notas_alunos)

# Item b
# Para cada aluno, calcula a média final
for i in range(5):
    notas_alunos[i].append(round(((sum(notas_alunos[i][1])/3) + (sum(notas_alunos[i][2])/3))/2, 2))

print(notas_alunos)


maior = notas_alunos[0][3]
# Item c
# Para cada aluno, procura o que tem a maior nota final
for i in range(1, 5):
    if notas_alunos[i][3] > maior:
        maior = notas_alunos[i][3]
        guarda_maior = i
print(f'O aluno que tirou a maior nota final foi o aluno {notas_alunos[guarda_maior][0]}. Ele tirou {notas_alunos[guarda_maior][3]}')

soma = 0
#Item d
# Calcula a média arimética das provas finais
for i in range(5):
    soma = soma + notas_alunos[i][3]
print(f'A média aritmética das notas finais {soma/5}')