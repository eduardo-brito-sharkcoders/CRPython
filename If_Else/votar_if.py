'''

    Desenvolver um programa que peça ao utilizador a sua idade,
    se a idade for maior ou igual a 18, pode votar.
    Se for menor a
    18 não pode votar.
    Também verificar se a idade não é menor que 0.

'''

idade = int(input("Insira a sua idade: "))

if idade >= 18:
	print("Pode votar!")
elif idade < 18 and idade >= 0:
	print("Ainda não pode votar.")
elif idade < 0:
	print("Não é possível ter idade negativa.")
else:
	print("O valor inserido, não corresponde ao pedido.")
