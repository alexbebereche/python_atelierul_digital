#1-5
"""
Meniu

"""

try:
    selectie = int(input("Introduceti un numar care sa apartina intervalului {1, 2, 3, 4, 5} : ")) #trebuie citit un numar, deci pe ramura else trebuie sa intre tot numere, altfel am exceptie
except ValueError:
    selectie = 0

if selectie == 1:
    print("Afisare lista de cumparaturi")
elif selectie == 2:
    print("Adugare element")
elif selectie == 3:
    print("Stergere element")
elif selectie == 4:
    print("Sterere lista de cumparaturit")
elif selectie == 5:
    print("Cautare in lista de cumparaturi")  #La fel ca 2
else:
    print("Alegerea nu exista. Reincercati")
