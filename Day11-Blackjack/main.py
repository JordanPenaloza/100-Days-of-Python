from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    player_cards = []
    bot_cards = []

    player_cards.append(draw_card())
    player_cards.append(draw_card())
    bot_cards.append(draw_card())
    bot_cards.append(draw_card())

    playing = True
    while playing:

        print(logo)

        player_score = calculate_score(player_cards)
        #player_cards, player_score = check_cards(player_cards, player_score)
        print(f"Your cards: {player_cards}, current score = {player_score}")

        bot_score = calculate_score(bot_cards)
        #bot_cards, bot_score = check_cards(bot_cards, bot_score)
        bot_first_hand = bot_cards[0]
        print(f"Bot's first hand: {bot_first_hand}")

        player_has_blackjack = check_blackjack(player_cards)
        bot_has_blackjack = check_blackjack(bot_cards)
        if player_has_blackjack and not bot_has_blackjack:
            print("Win! You have a blackjack!")
            
        elif bot_has_blackjack:
            print("Lose! Bot has a blackjack")
        
        if check_ace(player_cards):
            player_cards, player_score = check_cards(player_cards, player_score)
        elif check_ace(bot_cards):
            bot_cards, bot_score = check_cards(bot_cards, bot_score)
        
        while not check_gameover(player_score):
            draw_again = input("Would you like to draw another card? (y/n): ")
            if draw_again == 'y':
                player_cards.append(draw_card())
                print(f"Your cards: {player_cards}, current score = {player_score}")
                print(f"Bot's first hand: {bot_first_hand}")
            
                if bot_score < 17:
                    bot_cards.append(draw_card())
            else: 
                if bot_score < 17:
                    bot_cards.append(draw_card())

                print(f"Your final hand: {player_cards}, final score = {player_score}")
                print(f"Bot final hand: {bot_cards}, bot final score = {bot_score}")
                
                if player_score > bot_score:
                    print("You win!")
                elif player_score == bot_score:
                    print("Draw")
                else:
                    print("You lose!")
            
            if check_gameover(player_score):
                print(f"Your final hand: {player_cards}, final score = {player_score}")
                print(f"Bot final hand: {bot_cards}, bot final score = {bot_score}")
                print("You went over, you lose!")

            
        


        

def check_gameover(score):
    if score > 21:
        return True
    else:
        return False
    
def check_blackjack(cards):
    if 11 in cards and 10 in cards:
        return True
    else:
        return False

def check_ace(cards):
    if 11 in cards:
        return True
    else:
        return False
    
def check_cards(cards, score):
    for card in cards:
        if card == 11:
            if score > 21:
                card = 1
    score = calculate_score(cards)
    return cards, score
        
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


