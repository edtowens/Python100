# BlackJack Capstone
# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


def clear_scores():
    """Clears users and computers cards"""
    user_cards.clear()
    computer_cards.clear()


def update_ace_over_21(players_list):
    """Checks list for an ace and if sum of greater than 21 then convert ace to a value of 1"""
    for i in range(0, len(players_list)):
        if players_list[i] == 11:
            players_list[i] = 1
            break


def get_score(list_of_integers):
    """Gets a score from a list of cards"""
    score = 0
    for i in list_of_integers:
        score += i
    return score


def add_card(player_list):
    """Adds a card to a players list"""
    player_list.append(random.choice(cards))
    if get_score(player_list) > 21:
        update_ace_over_21(player_list)


def generate_computer_hand():
    """Generates the computers hand to completion"""
    computer_score = get_score(computer_cards)
    while computer_score <= 21:
        computer_score = get_score(computer_cards)
        if computer_score <= 16:
            add_card(computer_cards)
        else:
            break


def display_winner():
    """Displays winner and the statistics of the game"""
    user_score = get_score(user_cards)
    computer_score = get_score(computer_cards)
    if user_score > 21:
        print("Bust! Dealer Wins.")
        print(f"Your cards: {user_cards} score: {user_score}")
        print(f"Computer cards: {computer_cards} score: {computer_score}")
    elif user_score < computer_score <= 21:
        print("Dealer Wins!")
        print(f"Your cards: {user_cards} score: {user_score}")
        print(f"Computer cards: {computer_cards} score: {computer_score}")
    elif user_score == computer_score <= 21:
        print("Draw!")
        print(f"Your cards: {user_cards} score: {user_score}")
        print(f"Computer cards: {computer_cards} score: {computer_score}")
    else:
        print("You Win!")
        print(f"Your cards: {user_cards} score: {user_score}")
        print(f"Computer cards: {computer_cards} score: {computer_score}")


def blackjack():
    """Black Jack game main function"""
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != 'y':
        return
    else:
        os.system("clear")
        clear_scores()
    print(logo)
    # TODO-2: Draw cards for player and computer
    for i in range(1, 3):
        add_card(user_cards)
        add_card(computer_cards)

    # TODO-3: Show player current score and computers second card
    print(f"Your cards: {user_cards}, current score: {get_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    # TODO-4: Ask user if they want another card or to pass
    grab_another_card = True
    while grab_another_card:
        if get_score(user_cards) > 21:
            grab_another_card = False
            break
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            add_card(user_cards)
            print(f"Your cards: {user_cards}, current score: {get_score(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            grab_another_card = False

    # TODO-5: Runs computers hand to completion
    if get_score(user_cards) <= 21:
        generate_computer_hand()
    # TODO-6: Display winners and losers
    display_winner()
    blackjack()


blackjack()
