"""
Estruturas condicionais
if, else, elif

Exemplo em linguagem C

if (idade < 18) {
    printf ("Menor de idade")
else if (idade == 18)
    printf ("tem 18 anos")
else
    printf ("Maior de idade")
}

Em java:
    if (idade < 18) {
      System.out.println("Menor de idade")
    }
    else if (idade == 18) {
       System.out.println ("Tem 18 anos")
    }
    else{
       System.out.println("Maior de idade")
    }
"""
idade = 19

if idade < 18:
    print('Menor de idade')
    print(idade)
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
