"""
Levantando os próprios erros com Raise

raise -> Lança exceções

OBS: raise não é uma função. É uma palavra reservada.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.
A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

raise ValueError('Mensagem de Erro')

# Exemplo real
def colore(texto, cor):
    cores = 'verde', 'amarelo', 'azul', 'branco'
    if type(texto) is not str:
        raise TypeError(' Texto precisa ser uma string ')
    if type(cor) is not str:
        raise TypeError(' Cor precisa ser uma string ')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impressor na cor {cor}')


colore('True', 'preto')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado

"""

