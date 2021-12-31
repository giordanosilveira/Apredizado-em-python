"""
Sistemas de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt'))  # false
print(os.path.exists('frutas.txt'))  # True

# Diretório

# Paths relativos
print(os.path.exists('vasco')) # true
print(os.path.exists('vasco/../vai_corinthians'))  # False
print(os.path.exists('vasco/da_gama'))  # True
print(os.path.exists('outro'))  # false

# Paths absolutos
print(os.path.exists('/home/pingo/Documentos')) # true
print(os.path.exists('/home/pingo/VASCO')) # False
print(os.path.exists('/home/pingo/apps/jdk11')) # true

# Criando arquivos

# Forma 1
open('file.txt', 'w').close()

# Forma 2
open('file2.txt', 'a').close()

# Forma 3
with open('file3.txt', 'w') as arq:
    pass

# Forma 4 - "correta"
os.mknod('file4.txt')
os.mknod('/home/pingo/file.txt')

# se vocẽ estiver utilizando no MAC Os, pode haver um erro de PermissionError
# OBS: Se o arquivo já existir, teremos o erro FileExistsError

# Criando diretórios 

# um a um

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError
# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError

# Path Relativo
os.mkdir('corinthians')

# Path Absoluto
os.mkdir('/home/pingo/corinthians')

os.mkdir('etc/corinthians')

# multi-diretórios (árvore de diretórios)

# OBS: se já existir, teremos um FileExistsError
os.makedirs('corinthians/vai_corinthians/poropopó')
os.makedirs('outro/outro2/outro2', exist_ok=True)

# Renomenado arquivos e diretórios

# OBS: Se o diretório não existir, teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

os.rename('flamengo/da_gama', 'flamengo/malvadao')
os.rename('novo.txt', 'carlinho.txt')

# Removendo arquivos
# ATENÇÂO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vão para a lixeira. Eles somem.
# OBS: Se você estiver no Windows e o arquivo que você estiver em uso, você tera um erro
# OBS: CAso o arquivo não exista, teremos o FileNotFoundError
# OBS: Se você informar um diretório ao invés de uma arquivo, teremos um IsaADirectoryError

# os.remove('file.txt')
# os.remove('file2.txt')
# os.remove('file3.txt')
# os.remove('file4.txt')
os.remove('corinthians')

# Removendo diretórios vazios

os.rmdir('flamengo/malvadao')
# OBS: Se o diretório tiver qualquer conteúdo, teremos um OSError
# OBS: se o diretório não existir, teremos um FileNotFoundError

os.rmdir('flamengo')

# Removendo uma árvore de arquivos

for arquivo in os.scandir('nome_do_diretório'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios
# se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.
os.removedirs('caminho_dos_diretórios')

# Importando a lib send2trash
# Envia tando diretórios quanto arquivos para a lixeira
from send2trash import send2trash

os.remove('giba.txt')  # Não vai para a lixeira 

send2trash('carlinho.txt')  # vai para a lixeira
# OBS: Se o arquivo não existir teremos OSError    


# Trabalhando com arquivos e diretórios temporários

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrever um texto. No final, usamos um input() só para mantermos os 
# arquivos temporários 'ativos' dentro dos blocos with
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_tmp.txt'), 'w') as arq:
        arq.write('Eu não aguento mais porra\n')
    input()

# OBS: possivelmente, o código acima não irá funcionar se vocẽ estiver utilizando o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos
# temporários


# criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Giordano Silveira\n')
    tmp.seek(0)
    print(tmp.read())
    
# Em arquivos temporários, só conseguimos escrever bits. Por isso, utilizamos 'b'

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Giordano Silveira\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Giordano Silveira\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()

https://docs.python.org/3/os.html?highlight=os#module-os

"""

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

