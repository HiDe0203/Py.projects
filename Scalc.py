while True:
    calc =input("\n\n\nPick an operator: \nAdd (+) \nSubtract (-) \nMultiply (*) \nDivide (/) \npick one:")

    a = float(input("Enter a number:"))
    b = float(input("Enter a number:"))

    if calc == "+":
        print(a+b)

    elif calc == "-":
        print(a-b)

    elif calc == "*":
        print(a*b)

    elif calc == "/":
        print(a/b)
    else:
        print("please pick 1 of the 4 choices.")