lines = []
correct = {}
guess = {}
yellow = 0
green = 0

for i in range(6):
    lines += [input()]
correct_letters = ''
guess_letters = ''

for line in lines[:3]:
    for letter in line:
        correct[letter] = correct[letter] + 1 if letter in correct else 1
        correct_letters += letter
for line in lines[3:]:
    for letter in line:
        guess[letter] = guess[letter] + 1 if letter in guess else 1
        guess_letters += letter

for letter in guess:
    if letter in correct:
        if guess[letter] > correct[letter]:
            yellow += correct[letter]
        else:
            yellow += guess[letter]

for i in range(len(correct_letters)):
    if correct_letters[i] == guess_letters[i]:
        green += 1
        yellow -= 1

print(green)
print(yellow)
