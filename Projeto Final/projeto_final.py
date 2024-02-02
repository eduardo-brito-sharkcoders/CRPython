def _sum(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


def remainder(n1, n2):
    return n1 % n2


def is_even(n):
    return "even" if (n % 2) == 0 else "odd"


history = []

while True:

    print("1 - sum")
    print("2 - subtract")
    print("3 - multiply")
    print("4 - divide")
    print("5 - pow")
    print("6 - remainder")
    print("7 - even or odd")
    print("8 - history of operations")
    print("9 - exit")

    option = int(input("choose an option: "))

    # sum
    if option == 1:
        n1 = float(input("insert the first number: "))
        n2 = float(input("insert the second number: "))
        print(_sum(n1, n2))
        history.append(str(f"sum of {n1} and {n2} is {_sum(n1, n2)}"))

    # subtract
    elif option == 2:
        n1 = float(input("insert the first number: "))
        n2 = float(input("insert the second number: "))
        print(subtract(n1, n2))
        history.append(str(f"subtraction of {n1} and {n2} is {subtract(n1, n2)}"))

    # multiplication
    elif option == 3:
        n1 = float(input("insert the first number: "))
        n2 = float(input("insert the second number: "))
        print(multiply(n1, n2))
        history.append(str(f"multiplication of {n1} and {n2} is {multiply(n1, n2)}"))

    # division
    elif option == 4:
        n1 = float(input("insert the first number: "))
        n2 = float(input("insert the second number: "))
        print(divide(n1, n2))
        history.append(str(f"division of {n1} and {n2} is {divide(n1, n2)}"))

    # pow
    elif option == 5:
        n1 = float(input("insert the first number: "))
        n2 = float(input("insert the second number: "))
        print(power(n1, n2))
        history.append(str(f"{n1} to the power of {n2} is {power(n1, n2)}"))

    # remainder
    elif option == 6:
        n1 = float(input("insert the first number: "))
        n2 = float(input("insert the second number: "))
        print(remainder(n1, n2))
        history.append(str(f"remainder of {n1} and {n2} is {remainder(n1, n2)}"))

    # even or odd
    elif option == 7:
        n = int(input("insert a number: "))
        print(is_even(n))
        history.append(str(f"the number {n} is {is_even(n)}"))

    elif option == 8:
        for _ in history:
            print(_)

    elif option == 9:
        exit()

    else:
        print("Invalid option.")