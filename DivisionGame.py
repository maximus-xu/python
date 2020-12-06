
from python.utils import get_input2
import random

running = True
score = 0
incorrect_score = 0
problem_count = 0
incorrect_answers = []
while running:
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 10)

    if number1 > number2:
        if number1 % number2 != 0:
            remainder = number1 % number2
            answer = int((number1 - remainder) / number2)
            input_answer = get_input2(f"What's {number1} / {number2}? ")
            if input_answer == f"{answer} r {remainder}" or input_answer == f"{answer} R {remainder}":
                print("Correct!")
                score += 1
            elif input_answer.lower() == "quit":
                quit_input = input("Would you like to quit (y/n)? ")
                if quit_input.lower() == "y":
                    print("")
                    if incorrect_score == 1:
                        print("You have attempted 1 problem.")
                    else:
                        print(f"You have attempted {incorrect_score} problems.")
                    print(f"Your score is {score}.")
                    print(f"You have incorrectly attempted {incorrect_score} problems.")
                    if incorrect_score > 0:
                        print(f"Your incorrect answers are {incorrect_answers}.")
                    break
                else:
                    problem_count -= 1
            elif input_answer.lower() == "status" or input_answer.lower() == "score":
                print("")
                if incorrect_score == 1:
                    print("You have attempted 1 problem.")
                else:
                    print(f"You have attempted {incorrect_score} problems.")
                print(f"Your score is {score}.")
                print(f"You have incorrectly attempted {incorrect_score} problems.")
                if incorrect_score > 0:
                    print(f"Your incorrect answers are {incorrect_answers}.")
            else:
                print("Incorrect")
                print(f"The correct answer was {answer} R {remainder}")
                incorrect_score += 1
                incorrect_answers.append(str(number1) + " / " + str(number2) + " = " + str(answer) + " R "
                                         + str(remainder) + "; incorrect answer given: " + '"' + input_answer + '"')
            problem_count += 1


print("Thanks for playing.")