from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    print(logo)
    player_card1 = draw_card()
    player_card2 = draw_card()
    print(f"Your cards: [{player_card1}, {player_card2}]")


def draw_card():
    card = cards[random.randint(0,12)]
    return card




while input("Would you like to play a game of blackjack? (y/n): ") == "y":
    clear()
    play_game()


