#trebuia sa verific si daca e o data din viitor
#daca foloseam datetime, scapam de an bisect si chestii de genul



def an_bisect(an):
    try:
        an = int(an)
    except ValueError:
        an = -1

    if an >= 0:
        if an % 4 == 0:
            if an % 100 == 0:
                if an % 400 == 0:
                    return 0
                else:
                    return 0
            else:
                return 1
        else:
            return 0
    else:
        return 0

def control(cnp):
    nr = "279146358279"
    s = 0
    for i in range(len(cnp) - 1): #without taking C in consideration
        s += int(cnp[i]) * int(nr[i])
    if s % 11 == 10:
        return 1
    else:
        return s % 11

#cnp = input("Introdu un CNP: ")
cnp = "1990915412346"


#cnp = "19909154_2346"


#29 februarie - an bisect
#cnp = "1960229011238"

#29 februarie - an (ne)bisect
#cnp = "1950229011237"

#29 februarie - an bisect pentru ca se imparte la 100, fara sa se imparta la 400
# cnp = "2000229229998"

#aprilie - nu are 31 de zile - invalid
# cnp = "2000431229999"

#negativ
# cnp = "-2000430229996"

# cnp = "2141414asd"

cnp_list = list(cnp)
ok = 1

if '_' in cnp or '.' in cnp or 'e' in cnp or 'j' in cnp:
    ok = 0

if len(cnp.strip()) != 13:
    ok = 0
else:
    try:
        cnp = int(cnp)
        if cnp < 0:
            ok = 0
    except ValueError:
        ok = 0


cnp = str(cnp)

if len(cnp.strip()) != 13:
    ok = 0

if ok == 1:
    # S
    S = int(cnp_list[0])
    if S <= 0:
        ok = 0


    #LL
    #Luna
    LL = int(cnp_list[3]) * 10 + int(cnp_list[4])
    if LL < 1 or LL > 12:
        ok = 0


    #AA
    #Anul
    AA = int(cnp_list[1]) * 10 + int(cnp_list[2])
    if AA < 0 or AA > 99:
        ok = 0


    #ZZ
    #Ziua
    ZZ = int(cnp_list[5]) * 10 + int(cnp_list[6])
    if ZZ < 1:
        ok = 0

    if LL != 1 and LL != 3 and LL != 5 and LL != 7 and LL != 8 and LL != 10 and LL != 12: #mergea mai frumos cred
        if LL == 2:
            if S == 1 or S == 2 or S == 7 or S == 8 or S == 9:
                if an_bisect(19 * 100 + AA) == 0:
                    if ZZ > 28:
                        ok = 0
                else:
                    if ZZ > 29:
                        ok = 0

            if S == 3 or S == 4 or S == 5 or S == 6:
                if an_bisect(18 * 100 + AA) == 0:
                    if ZZ > 28:
                        ok = 0
                else:
                    if ZZ > 29:
                        ok = 0

        if ZZ > 30:
            ok = 0
    else:
        if ZZ > 31:
            ok = 0


    #JJ
    #Judet
    JJ = int(cnp_list[7]) * 10 + int(cnp_list[8])
    if JJ < 1 or JJ > 52:
        ok = 0

    #NNN
    #Numar format din 3 cifre din intervalul 001 - 999
    NNN = int(cnp_list[9]) * 100 + int(cnp_list[10]) * 10 + int(cnp_list[11])
    if NNN < 1 or NNN > 999:
        ok = 0

    #C
    #Cifra de control
    C = int(cnp_list[12])
    if C != control(cnp):
        ok = 0

if ok == 1:
    print("CNP-ul e valid")
else:
    print("CNP-ul nu e valid")

#print(control(cnp))