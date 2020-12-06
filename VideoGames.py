from math import ceil

from python.utils import get_input2, parse_input_int

import random, time
running = True
dinosaur = "Apatosaurus"
dinosaur_level = 1
food = 1000000
max_food_production = 1000
dinosaur_HP = 50
dinosaur_attack = 25
print("Welcome to Jurrassic World Alive!")
print("")
print(f"You have an {dinosaur} at level {dinosaur_level}.")
print(f"You have {food} food.")
while running:
    print("")
    option = get_input2("What would you like to do (make food, view dinosaurs, feed dinosaurs, battle)? ")
    if option.lower() == "make food":
        input_food = get_input2(f"How much food would you like to make (1-{max_food_production})? ")
        if parse_input_int(input_food) != "error":
            input_food = parse_input_int(input_food)
            if input_food <= max_food_production | input_food > 0:
                print("Making food...")
                time.sleep(1)
                food += input_food
                print(f"You now have {food} food.")
            elif input_food < 1:
                print(f"You can't make {input_food} food!")
            else:
                print(f"You can only make up to {max_food_production} food.")
                print("Please upgrade food production.")
    elif option.lower() == "view dinosaurs":
        print(f"You have an {dinosaur} at level {dinosaur_level}.")
        print(f"Your {dinosaur} has {dinosaur_HP} health and {dinosaur_attack} attack")
    elif option.lower() == "feed dinosaurs":
        if food >= dinosaur_level * 1000:
            print(f"Feeding {dinosaur.lower()}...")
            time.sleep(3)
            food -= dinosaur_level * 1000
            dinosaur_level += 1
            dinosaur_HP += 10
            dinosaur_attack += 5
            print(f"Your apatosaurus is now at level {dinosaur_level}")
        else:
            print("You do not have enough food.")
            print(f"You need {dinosaur_level * 1000 - food} more food.")
    elif option.lower() == "battle":
        print("")
        print(f"Your {dinosaur.lower()}'s health is {dinosaur_HP}.")
        print(f"Your {dinosaur.lower()}'s attack is {dinosaur_attack}.")
        if get_input2("Are you sure you want to battle (y/n)? ").lower() == "y":
            battle_HP = dinosaur_HP
            if random.randint(0, 2) == 0:
                enemy_HP = dinosaur_attack
                enemy_attack = dinosaur_HP
            else:
                enemy_HP = dinosaur_HP * 2
                enemy_attack = ceil(dinosaur_attack / 2)
            print("")
            print("Searching for a battle...")
            time.sleep(random.randint(1, 5))
            print("Battle starting!")
            print("")
            print(f"Your enemy's health is {enemy_HP} and their attack is {enemy_attack}.")
            time.sleep(1)
            attack_point = 0
            enemy_attack_point = 0
            shield_point = 0
            enemy_shield_point = 0
            hexagon_point = 0
            enemy_hexagon_point = 0

            while battle_HP > 0 and enemy_HP > 0:

                if hexagon_point == 0:
                    battle_option = get_input2('What would you like to do (attack, shield, hexagon)? ')
                else:
                    battle_option = get_input2('What would you like to do (attack, shield, hexagon)? ')
                    second_battle_option = get_input2('What else would you like to do (attack, shield)? ')

                if enemy_hexagon_point == 0:
                    enemy_option = random.randint(1, 3)
                else:
                    enemy_option = random.randint(1, 3)
                    second_enemy_option = random.randint(1, 2)
                # 1 = attack, 2 = shield, 3 = hexagon

                if battle_option or second_battle_option == 'attack':
                    attack_point += 1
                elif battle_option and second_battle_option == 'attack':
                    attack_point += 2

                if enemy_option or second_enemy_option == 1:
                    enemy_attack_point += 1
                elif enemy_option and second_enemy_option == 1:
                    enemy_attack_point += 2

                if battle_option or second_battle_option == 'shield':
                    shield_point += 1
                elif battle_option and second_battle_option == 'shield':
                    shield_point += 2

                if enemy_option or second_enemy_option == 2:
                    enemy_shield_point += 1
                elif enemy_option and second_enemy_option == 2:
                    enemy_shield_point += 2

                if battle_option == 'hexagon':
                    hexagon_point += 1
                if enemy_option == 3:
                    enemy_hexagon_point += 1

                if attack_point <= 1 and enemy_shield_point == 0:
                    print(f"You used {attack_point} attack!")
                    print("Enemy used no shield!")
                    enemy_HP -= attack_point * dinosaur_attack
                    print(f"Enemy now has {enemy_HP} health!")
                elif attack_point <= 1 and enemy_shield_point <= 1:
                    if enemy_shield_point == 1:
                        print(f"You used {attack_point} attack but enemy used 1 shield.")
                    if enemy_shield_point == 2:
                        print(f"YOu used {attack_point} attack but enemy used 2 shields.")
                    attack_point -= enemy_shield_point
                    if attack_point < 0:
                        attack_point = 0
                    enemy_HP -= dinosaur_attack * attack_point
                    if attack_point == 0:
                        print("You did no damage.")
                    else:
                        print(f"You did {dinosaur_attack * attack_point}")

                print("")

            if battle_HP == 0:
                print("Defeat")
            else:
                print("Victory!")
    else:
        print(f"You can't" + f' {option}')