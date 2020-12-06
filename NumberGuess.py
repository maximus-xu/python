
from python.utils import get_input

high = int(get_input("What's the range? ")) - 1
low = 1
running = True

while running:
    guess = (high + low) / 2
    print(f"My guess is {int(guess)}.")
    answer = str(input("Higher (H), Lower (L), Correct (C). "))

    if answer.lower() == "h":
        low = guess + 1
    elif answer.lower() == "l":
        high = guess
    elif answer.lower() == "c":
        print("I'm correct!")
        break
    else:
        print(f"{answer} is not a valid answer.")
