"""
Exemplo para a aula dunder.py
"""
import primeiro
def funcao2():
    primeiro.funcao1()
    
if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente.')
# Esse else não existe na prática, é só um exemplo
else:
    print(f'segundo.py for importado. {__name__}')
