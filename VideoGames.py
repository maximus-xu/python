
from python.utils import get_input2, parse_input_int

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
                