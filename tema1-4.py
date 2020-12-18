#1-4

numar = int(input("Introdu un numar: "))


if numar > 0:
    if numar < 10:
        print("Numarul este < 10") #Mentionez nimic daca e >= 10? Imi asum ca da
    else:
        print("Numarul este >= 10")
elif numar == 0:
    print("Numarul este 0")
else:
    numar = abs(numar)       #transform
    print(numar)             #afisez