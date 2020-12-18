#1-1
"""
consider ca un caracter este un caracter de la tastatura, cu exceptia cifrelor
pentru ca stiu automat ca un fct input returneaza string in orice caz
"""
nume = input("Numele tau este: ")
text = input("Introduce text: ")

if text.isdigit():
    print(f"Sirul de numere a fost gasit de {nume}")
elif text.isdigit() is False: #if-elif-else...
    print(f"Sirul de caractere a fost gasit de {nume}")
else:
    pass
