import random

word_list = ['amol','anuja','shubham']

chosen_word = random.choice(word_list)
print(chosen_word)
display=[]
for i in range(0,len(chosen_word)):
    display+='_'
print(display)
lives=6
print("you have 6 lives")

end_of_game=False

while not end_of_game:

    guess = input("guess the letter: ").lower()
    flag = False
    for pos in range(len(chosen_word)):
        letter=chosen_word[pos]
        if letter==guess:
            display[pos]=letter
            flag = True

    print(display)

    if not flag:
        lives-=1
        print(f"wrong guess. you have {lives} lives remaining")
        if lives==0:
            print("no lives left. you loose...:)")
            end_of_game=True

    if '_' not in display:
        end_of_game=True
        print("you win!!!!")
