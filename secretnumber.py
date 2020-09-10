secret = 29
guess = None
versuche = 0

print("Errate die geheime Zahl zwischen 1 und 50.")

while guess != secret:
    guess = int(input("Deine Zahl: "))
    versuche = versuche + 1
    if guess < secret:
        print("Diese Zahl war zu niedrig.")
    if guess > secret:
        print("Diese Zahl war zu hoch.")

print("Sehr gut! Du hast die geheime Zahl erraten. Es ist die " + str(secret) + ".")
print("Du hast " + str(versuche) + " Versuche gebraucht um die geheime Zahl zu entdecken!")
