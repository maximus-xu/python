import random
import click


def get_word_list():
    with open("word_list.txt") as file:
        raw = [line.strip('\n') for line in file.readlines()]
        return [word.lower() for word in raw if len(word) >= 3 and '-' not in word and '(' not in word]

#  o
# /|\
# / \
def draw(error):
    output = ''
    if error > 0:
        output += '  O'
    if error > 1:
        output += '\n  |'
    if error > 2:
        output = '  O\n--|'
    if error > 3:
        output += '--'
    if error > 4:
        output += '\n /'
    if error > 5:
        output += ' \\'
    # click.echo(click.style(output, fg='green'))
    click.secho(output, fg="red")


word_list = get_word_list()
word = random.choice(word_list)
letters = [letter for letter in word]
guesses = set()
current_guess = ["-"] * len(word)
remaining = 6
# print(word)
while current_guess != letters:
    print(''.join(current_guess))
    input_letter = input("input letter: ")
    if len(input_letter) != 1:
        print("invalid input")
        continue
    if input_letter in letters and input_letter not in guesses:
        for i in range(len(letters)):
            if input_letter == letters[i]:
                current_guess[i] = input_letter
    elif input_letter in guesses:
        print("you've already guessed this letter")
    else:
        remaining -= 1

    draw(6-remaining)

    if remaining == 0:
        print("FAIL")
        print(f"The correct answer was: {word}")
        exit(0)
    guesses.add(input_letter)

print("You win!")

# if correct fill word template

# if wrong guess print/add to hangman

# loop to "ask for input"

# continue until hangman drawn or word guessed

#  o
# -|-
# / \
