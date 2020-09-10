x = int(input("Gib den Wert für X ein: "))

y = int(input("Gib den Wert für y ein: "))

operation = input("Wähle deine Rechenoperation (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Entschuldigung, Unbekannte Rechenoperation")
