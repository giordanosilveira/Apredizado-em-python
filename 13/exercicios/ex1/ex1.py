"""
Enunciado:
No print da pasta
"""

def le_arq_por_char(arq):
    """Le um arquivo char por char e printa o char lido na tela
    Args:
        arq ([file]): Um arquivo
    """
    c = arq.read(1)
    while c:
        print(f'{c}')
        c = arq.read(1)


def escreve_arquivo(arq):
    entrada = input('Digite o que você quer no arquivo: ')
    while entrada != '0':
        arq.write(entrada+'\n')
        entrada = input()
         
if __name__ == '__main__':
    with open('arq.txt', 'w') as arq:
        escreve_arquivo(arq)
    
    with open('arq.txt') as arq:
        le_arq_por_char(arq)
         


