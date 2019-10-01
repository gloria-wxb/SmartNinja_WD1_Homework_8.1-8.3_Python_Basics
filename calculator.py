x = int(input("Please type any number: "))
y = int(input("And now a second one: "))

operation = input("Choose a math operation (+, -, /, *): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "/":
    print(x / y)
elif operation == "*":
    print(x * y)
else:
    print("Ups, your input was wrong.")