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

print(f"Sehr gut! Du hast die geheime Zahl erraten. Es ist die  {secret}.")

print(f"Du hast {versuche} Versuche gebraucht um die geheime Zahl zu entdecken!")
