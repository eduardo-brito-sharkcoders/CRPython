'''

Explicação If .. Else

se a condição for verdadeira:
    então fazer algo.
senão a condição é falsa:
    então fazer algo.

if <condição>:
    print("condição é verdadeira.")
else:
    print("condição é falsa.")

Explicação If .. Elif .. Else

se a condição_1 for verdadeira:
    então fazer algo_1
senão se a condição_2 for verdadeira:
    então fazer algo_2
senão se a condição_3 for verdadeira:
    então fazer algo_3
senão:
    então fazer algo


if <condição>:
    print("condição é verdadeira.")
else if <condição 2>:
    print("condição 2 é verdadeira.")
else if <condição 3>:
    print("condição 3 é verdadeira.")
else:
    print("condição é falsa.")

'''

condicao_1 = 5 == 5
condicao_2 = 98 >= 98
condicao_3 = 5 >= 5 + 1

if condicao_1:
    print("condicao 1 é verdadeira.")
elif condicao_2:
    print("condicao 2 é verdadeira.")
elif condicao_3:
    print("condicao 3 é verdadeira.")
else:
    print("nenhuma das condições é verdadeira.")