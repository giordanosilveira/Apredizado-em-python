"""
Geradores

- Generators (geradores) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

__________________________________________________________________________________________
|Funções                                       |Generators Functions                      |
------------------------------------------------------------------------------------------
- Utilizam return                              | - Utilizam yield
- Retorna uma vez                              | - Podem utilizam yield múltiplas 
                                               |   vezes
- Quando executada, retorna uma valor          | - Quando executada retorna um generator 

gen = conta_ate(5)
 
for num in gen:
    print(num)
      
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


"""

# Exemplo de Generator Function
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
        
# OBS: Uma generator function não é um Generator. Ela gera um generator.
gen = conta_ate(10)
print(next(gen))

print()

gen = list(conta_ate(10))
print(gen)