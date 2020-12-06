def reverse_string(input):
    output = ""
    index = -1
    count = len(input)
    while count != len(output):
        output += input[index]
        index -= 1

    return output


def parse_input_int(raw):
    try:
        return int(raw)
    except:
        return "error"


def parse_input_str(raw):
    try:
        return str(raw)
    except:
        return -1


def get_input(message):
    valid = False
    while not valid:
        raw_input = input(message)
        output = parse_input_int(raw_input)
        if output == "error":
            print("Please enter an integer value.")
        else:
            return output


def get_input2(message):
    valid = False
    while not valid:
        raw_input = input(message)
        output = parse_input_str(raw_input)
        if output == -1:
            print("Please enter a valid answer.")
        else:
            return output


def chicken_rabbit_problem():
    heads = float(input("How many heads: "))
    legs = float(input("How many legs: "))

    if legs % 2 != 0:
        print("Please enter an even value for legs.")
        exit(0)

    if (heads * 2 <= legs and heads * 4 >= legs) == False:
        print("Please check the values for legs.")
        exit(0)

    rabbits = legs / 2 - heads
    chickens = heads - rabbits

    print(f"Number of chickens is {int(chickens)}")
    print(f"Number of rabbits is {int(rabbits)}")


def prime_number_problem():
    number_list = [i for i in range(2, 100)]

    def remove_multiple(number_list_parameter):
        first = number_list_parameter[0]
        result = []
        for i in number_list_parameter:
            if number_list_parameter[0] % first != 0:
                result.append(number_list_parameter[0])

        return result

    for i in number_list:
        number_list = remove_multiple(number_list)
        print(number_list)


def number_guess_game_problem():
    high = int(input("What's the range? ")) - 1
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


def reverse_string_problem():
    string = "Hello World"
    string_list = string.split(" ")
    reversed_list = reverse_string(string)
    print(reversed_list)


def palindrome_problem():
    input_str = str(input("Enter: "))
    reversed_input = reverse_string(input_str)
    print(reversed_input == input_str)


def money_problem():
    money = get_input("How many cents? ")
    print(f"Number of pennies is {money % 25}.")
    print(f"Number of quarters is {int((money - (money % 25)) / 25)}.")


def two_coin_count_problem():
    cents = get_input("How many cents? ")
    mode = cents % 5
    print(f"There are {int((cents - mode) / 5) + 1} combination(s).")


def find_coin_count2(money, coin_list, result):
    if len(coin_list) == 1:
        print([money] + result)
        return 1

    largest_coin_value = coin_list[-1]
    sub_coin_list = coin_list[0:-1]
    largest_coin_count = 0
    total_count = 0
    while largest_coin_value * largest_coin_count <= money:
        rest_money = money - largest_coin_count * largest_coin_value
        total_count += find_coin_count(rest_money, sub_coin_list, [largest_coin_count] + result)
        largest_coin_count += 1

    return total_count


def find_coin_count(money, coin_list, box):
    if len(coin_list) == 1:
        print([int(money / coin_list[0])] + box)
        return 1

    *shortened_coin_list, largest_coin = coin_list
    number_of_largest_coin = 0
    number_of_coin_count = 0
    while money - largest_coin * number_of_largest_coin >= 0:
        number_of_coin_count += find_coin_count(money - largest_coin * number_of_largest_coin,
                                                shortened_coin_list,
                                                [number_of_largest_coin] + box)
        number_of_largest_coin += 1

    return number_of_coin_count


def division_game():
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


import random
running = True
dinosaurs = "Apatosaurus"
dinosaur_level = 1
food = 0
max_food_production = 1000
dinosaur_HP = 500
dinosaur_attack = 250
print("Welcome to Jurrassic World Alive!")
if get_input2("Press spacebar to start. "):
    while running:
        print("")
        print(f"You have these dinosaurs: {dinosaurs} at level {dinosaur_level}.")
        print(f"You have {food} food.")
        option = get_input2("What would you like to do (make food, feed dinosaurs, battle)? ")
        if option.lower() == "make food":
            input_food = get_input2("Type a number to make that much food. ")
            if parse_input_int(input_food) != "error":
                input_food = parse_input_int(input_food)
                if input_food <= max_food_production:
                    food += input_food
                else:
                    print(f"You can only make up to {max_food_production} food.")
                    print("Please upgrade food production.")
        elif option.lower() == "feed dinosaurs":
            if get_input2(f"Which dinosaur would you like to feed: {dinosaurs} ").lower() == "apatosaurus":
                if food >= dinosaur_level * 1000:
                    print("Feeding apatosaurus...")
                    food -= dinosaur_level * 1000
                    dinosaur_level += 1
                    dinosaur_HP += 100
                    dinosaur_attack += 50
                    print(f"Your apatosaurus is now at level {dinosaur_level}")
                else:
                    print("You do not have enough food.")
                    print(f"You need {food - dinosaur_level * 1000} more food.")
        elif option.lower() == "battle":
            print(f"Your dinosaur's health is {dinosaur_HP}.")
            print(f"Your dinosaur's attack is {dinosaur_attack}.")
            if get_input2("Are you sure you want to battle (y/n)?").lower() == "y":
                enemy_HP = 400
                enemy_attack = 300
                print("Searching for a battle...")
                print("Battle starting!")
                print("")
                