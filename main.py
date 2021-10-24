from random import choice
from colorama import Fore, Style

with open("words.txt", "r") as f:
    random_word = choice(f.readlines())
    word_to_guess = "".join(random_word[:-1]).lower()

# print(word_to_guess)

tries = len(word_to_guess) * 2
print(f"Bienvenue dans le jeu du pendu ! \nVous avez {tries} tentatives pour touver le mot !")

user_word = ""
displayed_word = "".join("_ " for _ in word_to_guess)
wrong_letters = []

while tries > 0:
    print("\nLe mot à deviner est : ", displayed_word)
    print(f'Voici les lettres qui ne sont pas correcte : {wrong_letters}')

    user_input = input("Entrez une lettre : ")[0:1].lower()

    if user_input == "":
        print(Fore.RED + "-> Merci d'entrer une lettre ! <-")
        print(Style.RESET_ALL)
    elif user_input in word_to_guess:
        user_word += user_input
        print(Fore.GREEN + "-> Tu as trouvé une lettre ! <-")
        print(Style.RESET_ALL)
    else:
        tries -= 1
        print(Fore.RED + "-> Cette lettre n'est pas dans le mot <-\n")
        print(Style.RESET_ALL)
        wrong_letters.append(user_input)
    displayed_word = ""

    for x in word_to_guess:
        displayed_word += x + " " if x in user_word else "_ "

    if "_" not in displayed_word:
        print(Fore.GREEN + "-> C'est gagné! <- \nBravo à toi !")
        print(Style.RESET_ALL)
        break

if tries == 0:
    print(Fore.RED + f"-> C'est perdu :( \nTu n'as plus de tentatives \nLe mot à deviner était : {word_to_guess}")
    print(Style.RESET_ALL)