print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

option = int(input("> "))

if option == 1:
    n1 = float(input("Insira o primeiro valor: "))
    n2 = float(input("Insira o segundo valor: "))
    print(f"{n1 + n2}")

if option == 2:
    n1 = float(input("Insira o primeiro valor: "))
    n2 = float(input("Insira o segundo valor: "))
    print(f"{n1 - n2}")

if option == 3:
    n1 = float(input("Insira o primeiro valor: "))
    n2 = float(input("Insira o segundo valor: "))
    print(f"{n1 * n2}")

if option == 4:
    n1 = float(input("Insira o primeiro valor: "))
    n2 = float(input("Insira o segundo valor: "))
    print(f"{n1 / n2}")

else:
    print("Operação inválida.")
