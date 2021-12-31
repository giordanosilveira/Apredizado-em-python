"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError:
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo
+ -> Abre para o modo de atualização: leitura e escrita.

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado, Caso exista, o novo conteúdo será adicionada ao final.
# Exemplo x
try: 
    with open('silveira.txt', 'x') as arq:
        arq.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo a
with open('frutas.txt', 'a') as arq:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arq.write(fruta)
            arq.write('\n')
        else:
            break

# Exemplo r+ -> Temos controle do cursos se utilizarmos com o 'r' ou 'w'
with open('novo.txt', 'r+') as arq:
    arq.write('LOL.\n')
    arq.write('WTF.\n')
    arq.write('BBQ.\n')

# OBS: O 'a' SEMPRE escreverá no final do arquivo. Mesmo se você mover o cursor
with open('frutas.txt', 'a') as arq:
    arq.seek(0)
    arq.write('maracujá\n')
    arq.write('limão\n')

https://docs.python.org/3/library/functions.html#open

"""


        

