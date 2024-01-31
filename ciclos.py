while True:
    idade = int(input("Insira a sua idade: "))

    if idade >= 18:
        print("Pode votar!")
    elif idade < 18 and idade >= 0:
        print("Ainda não pode votar.")
    elif idade < 0:
        print("Não é possível ter idade negativa.")
    else:
        print("O valor inserido, não corresponde ao pedido.")