print("1 - Calcular Área;")
print("2 - Calcular Perímetro;")

option = int(input("Insira a opção desejada: "))

if option == 1:
    lado = float(input("insira o lado do quadrado: "))
    area = lado ** 2
    print(f"Area: {area}")

elif option == 2:
    lado = float(input("insira o lado do quadrado: "))
    perimetro = lado * 4
    print(f"Perimetro: {perimetro}")

else:
    print("Opção inválida")