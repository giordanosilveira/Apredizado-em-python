"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer o uso do módulo os.

os -> Operating System - Sistema Operacional

# gercwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # /home/pingo/Documentos/Apredizado-em-python/13

# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd()) # /home/pingo/Documentos/Apredizado-em-python/

os.chdir('..')
print(os.getcwd()) # /home/pingo/Documentos/

os.chdir('..')
print(os.getcwd()) # /home/pingo/

os.chdir('..')
print(os.getcwd()) # /home

os.chdir('..')
print(os.getcwd()) # /

os.chdir('..')
print(os.getcwd()) # /

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('/home/pingo/'))

# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows, terá que ter cuidado ao verificar diretórios.

# print(os.path.isabs('C:\\Users\\diretorio'))

# Podemos identificar o sistema operacional com o módulo os
# print(os.name) # posis (linus e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
# print(os.uname())

# Fazer o import
import sys
print(sys.platform)

'/home/geek/workspace/sistema'
print(os.getcwd())  # /home/pingo/Documentos/Apredizado-em-python/13
res = os.path.join(os.getcwd(), 'vasco', 'da_gama')
os.chdir(res)
print(os.getcwd())

# veja que o os.python.join() recebe dois parâmetro, sendo o primeiro o diretório atual e o segundo o diretório que será juntado ao atual

# podemos listar os arquivos e diretórios com o listdir()
print(len(os.listdir('/etc')))

"""

import os
# podemos listar os arquivos e diretórios com mais detalhes com scandir()
scanner = os.scandir('/etc')
arquivos = list(scanner)

# No meu caso
print(arquivos[0].inode())  # 46663313 -> Identificador do elemento na árvore de diretórios
print(arquivos[0].is_dir())  # É um diretório ? False
print(arquivos[0].is_file())  # É um arquivo ? True
print(arquivos[0].is_symlink())  # É um link simbólico ? False
print(arquivos[0].path)  # caminho até o arquivo /etc/magic

print(arquivos[0].stat())  # Estatísticas sobre o arquivo:
# os.stat_result(st_mode=33188, st_ino=46663313, st_dev=64769, st_nlink=1, st_uid=0, st_gid=0, st_size=111, st_atime=1605820866, st_mtime=1605820866, st_ctime=1640811176)

print(arquivos[0].name) # nome do arquivo

#OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo
scanner.close()