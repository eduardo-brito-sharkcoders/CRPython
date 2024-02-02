from random import randint

n = randint(0, 6)

print(n)

value = int(input("Insira um número (0 a 5): "))

if value == n:
    print("Vitória!")
else:
    print("Derrota.")