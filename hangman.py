"""
Jocul spanzuratoarea - 8 incercari
Reguli: Nu se vor vizualiza incercarile precedente
"""


import getpass


def listToString(s):
    str1 = ""

    for l in s:
        str1 += l

    return str1


NO_OF_TRIES = 8
try_number = 0


while True:
    word = getpass.getpass(prompt="Enter the word: ")
    if word != "" and word.isalpha():
        if len(word) <= 8:
            break
        else:
            print("Length is too big, the game can't be won!")
            continue

word = word.upper()

word_with_guesses = ""

for w in word:
    word_with_guesses += "."
word_with_guesses = list(word_with_guesses)
print(listToString(word_with_guesses))

won = False

#
tries_left = 0

while NO_OF_TRIES - try_number > 0 and listToString(word_with_guesses) != word:
    tries_left = NO_OF_TRIES - try_number
    print(f"You have {tries_left} tries left")
    while True:
        print()
        letter = str(input("Guess a letter: "))
        if len(letter) == 1 and letter.isalpha():
            break
        else:
            continue

    letter = letter.upper()

    i = 0
    ok = 0
    for w in word:
        if word[i] == letter:
            word_with_guesses[i] = letter
            ok = 1

        i += 1

    if ok == 1:
        print(f"Correct letter! ({letter})")
    else:
        print("Wrong letter!")
        try_number += 1

    # word_print = str(word_with_guesses)
    word_print = listToString(word_with_guesses)
    print(f"The guessed word so far is {listToString(word_print)}")
    # try_number += 1
    if listToString(word_with_guesses) == word:
        won = True

#
tries_left -= 1

print("The word is: " + listToString(word))

if tries_left != 0 or won is True:
    print("--------------You won!---------------")
else:
    print("You lost")