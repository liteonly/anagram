from game import Game
import random
import sys

def print_logo():
    print("===========")
    print("# ANAGRAM #")
    print("===========")

def baseless():
    if n_rounds > 100:
        gameplay = input(f"{n_rounds-round-1} rounds to go. Want to continue ? y/n \n")
        # print(gameplay)
        if gameplay.lower() == 'y':
            game.end_game()
            sys.exit(0)

game = Game()
if __name__ == '__main__':
    print_logo()
    print()
    text = input("Enter Number of Rounds: ")  # Python 3
    n_rounds = eval(text)
    if n_rounds == -1:
        n_rounds = 1000
    game.start_game(n_rounds)

    for round in range(n_rounds):
        n_chances = 3
        game.start_round()
        while n_chances > 0:
            guess = input()
            if game.check_user_guess(guess):
                n_chances = 0
                continue
            n_chances -= 1
    game.end_game()

