"""
Módulos Externos:

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.ord

colorama -> utilizado para permitir impressão de textos coloridos no terminal


Instalando um módulo

pip install <nome do módulo>


# installar o pdf-python primeiro
import pydf

pdf = pydf.generate_pdf('<h1>Giordano Silveira</h1><br/><br/><strong>Programa&ccedil;&atilde;o em python: Essencial</strong>')

with open('giba.pdf', 'wb') as f:
    f.write(pdf)
"""
# installar o colorama primeiro (pip install colorama)
#Utilizando o pacote colorama
from colorama import init, Fore

init()
print(Fore.MAGENTA + 'Giordano Silveira')
print(Fore.BLUE + 'Giordano Silveira')


