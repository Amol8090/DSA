import random

def deal_card():
    deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(deck)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user_score,comp_score):
    if user_score>21 and comp_score>21:
        return ("you gone over. you lose!!")

    if comp_score==user_score and user_score <21:
        return (f"its a draw in the game with same score : {comp_score}")

    elif comp_score==0:
        return ("you loose, opponent has blackjack")
    elif user_score==0:
        return ("you win!!, you have blackjack")
    elif user_score>21:
        return ("you gone over you lose")
    elif comp_score>21:
        return ("oppenent gone over, you win")
    elif user_score>comp_score:
        return ("you win")
    else:
        return "you lose"



user_cards=[]
comp_cards=[]

is_gameover=False
for i in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

while not is_gameover:
    user_score=(calculate_score(user_cards))
    comp_score=(calculate_score(comp_cards))

    print(f"your cards {user_cards}, current score = {user_score}")
    print(f"computer's first card {comp_cards[0]}")

    if user_score ==0 or comp_score==0 or user_score>21:
        is_gameover=True

    else:
        user_should_deal=input("type 'y' to get another card, type 'n' to pass").lower()
        if user_should_deal=='y':
            user_cards.append(deal_card())
        else:
            is_gameover=True

while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
print(compare_score(user_score, comp_score))

import os
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')    

