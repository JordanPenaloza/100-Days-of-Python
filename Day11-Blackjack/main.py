from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
bot_cards = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    print(logo)
    player_cards.append(draw_card())
    player_cards.append(draw_card())
    player_score = calculate_score(player_cards)
    print(f"Your cards: {player_cards}, current score = {player_score}")

def draw_card():
    card = cards[random.randint(0,12)]
    return card

def calculate_score(cards):
    score = 0
    for card in cards:
        score += card
    return score




while input("Would you like to play a game of blackjack? (y/n): ") == "y":
    clear()
    play_game()


