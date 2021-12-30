"""
Exemplo para a aula dunder.py
"""
def funcao1():
    print('Giordano Henrique Silveira')

if __name__ == '__main__':
    print('primeiro.py está sendo executado diretamente')
# Esse else não existe na prática, é só um exemplo
else:
    print(f'primeiro.py foi importado. {__name__}')    