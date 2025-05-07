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


#  Função que desenha a forca na tela

def display_hangman(chances):

    # Lista de estagios
    stages = [
        # estagio 6 (final)
        """
            ----------
            |        |
            |        O
            |       \\|/
            |        |
            |       / \\
            |
            -
        """,
        # estagio 5
        """
            ----------
            |        |
            |        O
            |       \\|/
            |        |
            |       / 
            |
            -
        """,
        # estagio 4
        """
            ----------
            |        |
            |        O
            |       \\|/
            |        |
            |       
            |
            -
        """,
        # estagio 3
        """
            ----------
            |        |
            |        O
            |       \\|
            |        |
            |       
            |
            -
        """,
        # estagio 2
        """
            ----------
            |        |
            |        O
            |        |
            |        |
            |       
            |
            -
        """,
        # estagio 1
        """
            ----------
            |        |
            |        O
            |       
            |       
            |       
            |
            -
        """,
        # estagio 0
        """
            ----------
            |        |
            |       
            |       
            |       
            |       
            |
            -
        """
    ]
    return stages[chances]


# Função do jogo
def game():

    limpaTela()

    print("\nBem vindo ao jogo da forca!")
    print ("Adivinhe a palavra abaixo: \n")

    # Lista de Palavras para o jogo

    palavras = ["banana", "abacate", "uva", "morango", "laranja"]

    # Escolhe randomicamente a palavra
    palavra = random.choice(palavras)

    # List de letras da palavra
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Numero de chances
    chances = 6

    # Lista para letras erradas

    letras_tentativas = []

    # Loop enquanto número de chances for maior que zero
    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional para verificar se foi digitado somente uma letra
        if len(tentativa) > 1 or not tentativa.isalpha():
            print("Você só pode digitar uma letra!!!")
            continue

        # condicional para verificar se já foi digitado a letra
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue
        # lista de tentativa
        letras_tentativas.append(tentativa)

        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")

            # Loop
            for indice in range(len(lista_letras_palavras)):

                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
                
            if "_" not in tabuleiro:
                print("\nVocê venceu!!! A palavra era: {}".format(palavra))
                break
        else:
                print("Ops. Essa letra não está na palavra!")
                chances -= 1
                
    if "_" in tabuleiro:
        print("\n###Você perdeu!! A palavra era: {}.".format(palavra)+"######")

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você esta apredendo programação em Python. :)\n")