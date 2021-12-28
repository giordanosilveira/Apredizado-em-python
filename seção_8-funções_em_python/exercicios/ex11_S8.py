"""
Enunciado:

Elabore uma função que receba três notas de um aluno como parâmetro e uma letra.
Se a letra for A, a função deverá calcular a Média aritimética das notas do aluno; se for P, deverá calcular
a média ponderada, com pesos 5, 3 e 2
"""


def testa_notas_alunos():
    """
    Testa o input do usuário para ver se ele digitou uma nota correta
    :return: Retorna uma lista contendo a nota do aluno
    """
    nota = []
    i = 0
    while i < 3:
        try:
            valor = float(input(f'{i + 1}º nota do aluno '))
        except ValueError:
            print('A nota deve ser um número ')
        else:
            i += 1
            nota.append(valor)
    return nota


def testa_ordem():
    """
    Teste para ver se o usuário digitou uma opção válida.
    :return: A opção que o usuário solicitou. Ou 'A' ou 'P'
    """
    ordem = input("Digite 'A' se quer a média aritimética ou 'P' se quer a média ponderada ")
    while ordem != 'A' and ordem != 'P':
        if ordem == 'a':
            aux = ordem.upper()
            ordem = aux
        elif ordem == 'p':
            aux = ordem.upper()
            ordem = aux
        else:
            ordem = input(f'{ordem} não é nenhuma opcão aceita. Digite uma opção válida ')
    return ordem


def calcula_media(notas, ordem='A'):
    """
    Calcula ou a média ponderada ou a média aritmética. Por default calcula a média aritimética
    :param notas: Notas do aluno
    :param ordem: 'A' se ele quer a média aritimérica, 'P' se quer a ponderada
    :return: Retorna a média aritimética ou a média ponderada
    """
    if ordem == 'A':
        return sum(notas)/3
    else:
        return (notas[0]*5 + notas[1]*3 + notas[2]*2)/10


notas = testa_notas_alunos()
ordem = testa_ordem()
if ordem == 'P':
    print(f'A média ponderada das notas é igual a {calcula_media(notas, ordem)}')
else:
    print(f'A média aritimética das notas é igual a {calcula_media(notas, ordem)}')
