import random, sys, time, os

# war game program


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}_{self.suit}"


class Deck:
    def __init__(self):
        suits = ["H", "D", "C", "S"]  # Hearts, Diamonds, Clubs, Spades
        ranks = [
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
        ]  # 11: Jack, 12: Queen, 13: King, 14: Ace
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def dsplit(self):
        half = len(self.cards) // 2
        return self.cards[:half], self.cards[half:]


def main():
    while True:
        user_input = input("Start the game? Y/N: ").lower()
        if user_input == "y":
            init_game()
            break
        elif user_input == "n":
            sys.exit("Bye!")
        else:
            print("Invalid input. Please enter Y or N.")

def init_game():
    deck = Deck()
    print("\nCreating a deck\n")
    for i in [".", ".", ".", " Deck created.\n"]:
        sys.stdout.write(str(i) + " ")
        sys.stdout.flush()
        time.sleep(0.5)

    deck.shuffle()
    print("\nShuffling\n")
    for i in [".", ".", ".", " Deck shuffled.\n"]:
        sys.stdout.write(str(i) + " ")
        sys.stdout.flush()
        time.sleep(0.5)

    player1_deck, player2_deck = deck.dsplit()
    print("\nDealing cards to players\n")
    for i in [".", ".", ".", " Deck dealt for Player 1 and Player 2.\n"]:
        sys.stdout.write(str(i) + " ")
        sys.stdout.flush()
        time.sleep(0.5)

            print("\nPlaying")
            winner, rounds, wars = play_war(player1_deck, player2_deck)
            for i in [".", ".", "."]:
                sys.stdout.write(str(i)+' ')
                sys.stdout.flush()
                time.sleep(0.5)
            print("\n")            
            print(f"{winner} won the game after {rounds} rounds and {wars} wars.\n")

def play_war(deck1, deck2):
    ...
    return winner, rounds, wars




if __name__ == "__main__":
    main()
