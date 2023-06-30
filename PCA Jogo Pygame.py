from palavras import *
import random

letras_usuario = []

chances = 7

ganhou = False

palavra = random.choice(palavra)

while True:

    dica_palavra(palavra)

    print(f'Já foram usadas as letras: {letras_usuario}')

    for letra in palavra:

        if letra.lower() in letras_usuario:

            print(letra, end=" ")

        else:

            print("_", end=" ")

    print(f"\n\nVocê tem \033[1;33m{chances} chances\033[m\n")

    if chances == 7:
        print("  _______     ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif chances == 6:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif chances == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif chances == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif chances == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif chances == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif chances == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        print(" |            ")
        print("_|___         ")
        print()


    elif chances == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()


    tentativa = input("Escolha uma letra para adivinhar: ")
    print(linha())

    letras_usuario.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():

        chances -= 1

    ganhou = True

    for letra in palavra:

        if letra.lower() not in letras_usuario:

            ganhou = False

    if chances == 0 or ganhou:

        break

if ganhou:

    print(f"Parabéns, você ganhou. A palavra era: {palavra}")

else:

    print(f"Você perdeu! A palavra era: {palavra}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("      \033[1;31mGAME OVER!!!\033[m")
    print(linha())
