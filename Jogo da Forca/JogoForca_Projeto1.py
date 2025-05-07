# Import

import random
from os import system, name

# Função para limpar a tela a cada execução

def limpaTela():

    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')


# Função
def game():

    limpaTela()

    print("\n Bem vindo ao jogo da forca!")
    print ("Adivinhe a palavra abaixo: \n")

    # Lista de Palavras para o jogo

    palavras = ["banana", "abacate", "uva", "morango", "laranja"]

    # Escolhe randomicamente a palavra
    palavra = random.choice(palavras)

    # List Comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Numero de chances
    chances = 6

    # Lista para letras erradas

    letras_erradas = []

    # Loop enquanto número de chances for maior que zero
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\n Chances restantes: ", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional

        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
                chances -= 1
                letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("\n Você venceu, a palavra era: ", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você esta apredendo programação em Python. :)\n")