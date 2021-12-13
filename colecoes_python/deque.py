"""
Módulo Collection - Deque

Podemos dizer que o Deque é uma lista de alta performance.

deq = deque('Giordano Henrique Silveira')
print(deq)

# Adicionando no deque
deq.append(' ')  # Aciciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo
print(deq)

# Removendo do deque
print(deq.pop())  # Removendo o último elemento e o retorna
print(deq)

print(deq.popleft())  # Removendo o primeiro elemento o retorna
print(deq)
"""
from collections import deque

