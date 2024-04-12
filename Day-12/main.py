import random

print("Welcome to number guessing game")
print("I am thinkinh a number between 1 and 100 ")
num = random.randint(1,50)

def play_game(chances):
    
    while chances>0:
        print(f"you have {chances} chnaces left to guess the number ")
        guess = int(input("Guess the number: "))
        if guess>num:
            chances-=1
            print("too high")
        elif guess < num:
            chances-=1
            print("too low")
        elif guess==num:
            print("you guesssed correct!!")
            return



level=input("choose a difficulty level 'easy' or 'hard': ").lower()

if level=='easy':
    play_game(10)
else:
    play_game(5)

print(num)
