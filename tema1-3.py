#1-3

an = int(input("Introdu un an: "))

def an_bisect(an):
    try:
        an = int(an)
    except ValueError:
        an = -1

    if an >= 0:
        if an % 4 == 0:
            if an % 100 == 0:
                if an % 400 == 0:
                    print(f"Anul {an} e an bisect")
                else:
                    print(f"Anul {an} NU e an bisect")
            else:
                print(f"Anul {an} e an bisect")
        else:
            print(f"Anul {an} NU e an bisect")
    else:
        print("Introdu un an bun")

an_bisect(an)