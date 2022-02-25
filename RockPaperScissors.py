import random


def win(choice1, choice2):
    win_choices = [["r", "s"], ["s", "p"], ["p", "r"]]
    if choice1 == choice2:
        return "tie"
    if [choice1, choice2] in win_choices:
        return "you win"
    return "you lose"


while True:
    choices = ['r', 'p', 's']
    player_choice = input("what's your choice (r/p/s) ").lower()
    if player_choice not in choices:
        print("you were kicked for cheating")
        exit(0)
    # choice = choices[random.randint(0, 2)]
    choice = random.choice(choices)
    print(choice)
    print(win(player_choice, choice))
