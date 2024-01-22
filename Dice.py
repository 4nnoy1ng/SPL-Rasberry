import random

def wurf():
    return random.randint(1, 6)

def spiel():
    print("Willkommen zum Würfelspiel gegen den Computer!")
    spieler_wins = 0
    computer_wins = 0

    for _ in range(6):
        input("Drücke Enter, um zu würfeln...")
        spieler_augen = wurf()
        computer_augen = wurf()

        print(f"Du hast eine {spieler_augen} geworfen, der Computer hat eine {computer_augen} geworfen.")

        if spieler_augen > computer_augen:
            print("Du gewinnst diese Runde!")
            spieler_wins += 1
        elif spieler_augen < computer_augen:
            print("Der Computer gewinnt diese Runde.")
            computer_wins += 1
        else:
            print("Unentschieden!")

    print("\nSpiel beendet!")
    if spieler_wins > computer_wins:
        print(f"Du hast insgesamt {spieler_wins} Runden gewonnen, der Computer hat {computer_wins} Runden gewonnen. Du gewinnst das Spiel!")
    elif spieler_wins < computer_wins:
        print(f"Du hast insgesamt {spieler_wins} Runden gewonnen, der Computer hat {computer_wins} Runden gewonnen. Der Computer gewinnt das Spiel.")
    else:
        print(f"Das Spiel endet unentschieden. Du hast {spieler_wins} Runden gewonnen, der Computer hat {computer_wins} Runden gewonnen.")

if __name__ == "__main__":
    spiel()
