"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em uma arquivo, após abrir o arquivo, utilizamos a função write(). Está função recebe uma string como parâmetro, caso contrário teremos
TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma,
todo o conteúdo no arquivo anterior é perdida

# Exemplo de escrita - modo 'w' - write (escrita)
with open('novo.txt', 'w') as arq:
    arq.write('Novos dados.\n')
    arq.write('Vasco da gama.\n')
    arq.write('Esta é a última linha.\n')

# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer\n')
arquivo.write('Mais um texto')

arquivo.close()

# Mais exemplos
with open('giba.txt', 'w') as giba:
    giba.write('giba ' * 1000)
"""
with open('frutas.txt', 'w') as arq:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arq.write(fruta)
            arq.write('\n')
        else:
            break
        


