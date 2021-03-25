from math import ceil, floor

from utils import get_input2, parse_input_int

import random, time


def get_enemy_option(range1, range2):
    return random.randint(range1, range2)


class BattleOption:
    ATTACK = 'attack'
    ATTACK_NUMBER = '1'
    SHIELD = 'shield'
    SHIELD_NUMBER = '2'
    HEXAGON = 'hexagon'
    HEXAGON_NUMBER = '3'


class EnemyBattleOption:
    ATTACK = 1
    SHIELD = 2
    HEXAGON = 3


class Dinosaur:
    APATOSAURUS = "Apatosaurus"


running = True
dinosaur = Dinosaur.APATOSAURUS
dinosaur_level = 1
food = 1000
coins = 100
dinobucks = 10
food_production_level = 1
max_food_production = food_production_level * 1000
dinosaur_HP = 50
dinosaur_attack = 25
victories = 0
coin_victories = 0
dinobuck_victories = 0
defeats = 0
total_battles = 0
print("Welcome to Jurrassic World Alive!")
print("")
print(f"You have an {dinosaur} at level {dinosaur_level}.")
print(f"You have {food} food.")

while running:
    print("")
    option = get_input2("What would you like to do (make food (1), upgrade (2), view inventory (3), "
                        "view dinosaurs (4), feed dinosaurs (5), battle (6))? ")
    if option.lower() == "make food" or option == '1':
        input_food = get_input2("Activate food production how many times? ")
        if parse_input_int(input_food) != "error":
            input_food = parse_input_int(input_food) * 1000
            if input_food > max_food_production:
                print(f"You can't make {input_food} food.")
                print("Please upgrade food production.")
            else:
                if get_input2(f"Are you sure you want to make {input_food} food (y/n)?"
                              f" It will cost you {int(input_food/20)} coins. ") == 'y':
                    if input_food/20 > coins:
                        print("You don't have enough coins.")
                        print(f'You need {int(input_food/20 - coins)} more coins.')
                    else:
                        print("Making food...")
                        time.sleep(input_food/1000)
                        food += input_food
                        coins -= int(input_food/20)
                        print(f"You now have {food} food.")
                        print(f"You now have {coins} coins.")

    elif option.lower() == "upgrade" or option == '2':
        input_upgrade = get_input2("What would you like to upgrade (food production (1))? ")
        if input_upgrade == 'food production' or input_upgrade == '1':
            if get_input2(f"Are you sure you want to upgrade food production (y/n)? It will cost you "
                          f"{food_production_level * 100} coins. ") == 'y':
                if food_production_level * 100 > coins:
                    print("You don't have enough coins.")
                    print(f"You need {food_production_level * 100 - coins} more coins")
                else:
                    upgrade_time = 0
                    time_remain = food_production_level * 5
                    print("Upgrading food production...")
                    while upgrade_time < food_production_level * 5:
                        print(f'{int(time_remain)} sec remaining')
                        upgrade_time += 1
                        time_remain -= 1
                        time.sleep(1)
                    coins -= food_production_level * 100
                    food_production_level += 1
                    max_food_production = food_production_level * 1000
                    print(f"Food production is now at level {food_production_level}.")
    elif option.lower() == "view inventory" or option == '3':
        print(f"You have {food} food.")
        print(f"You have {coins} coins.")
        print(f"You have {dinobucks} dinobucks.")
    elif option.lower() == "view dinosaurs" or option == '4':
        print(f"You have an {dinosaur} at level {dinosaur_level}.")
        print(f"Your {dinosaur} has {dinosaur_HP} health and {dinosaur_attack} attack")
    elif option.lower() == "feed dinosaurs" or option == '5':
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
    elif option.lower() == "battle" or option == '6':
        print("")
        print(f"Your {dinosaur.lower()}'s health is {dinosaur_HP}.")
        print(f"Your {dinosaur.lower()}'s attack is {dinosaur_attack}.")
        if get_input2("Are you sure you want to battle (y/n)? ").lower() == "y":
            battle_HP = dinosaur_HP
            difficulty = get_input2("What difficulty would you like to do (easy (1), medium (2), hard (3)) ")
            enemy_attack = -1
            while enemy_attack < 15:
                random_stats = random.randint(-10, 10)
                if difficulty == 'easy' or difficulty == '1':
                    difficulty = 1
                    enemy_HP = floor(dinosaur_HP * 1.5) + random_stats
                    enemy_attack = floor(dinosaur_attack / 3) - random_stats / 2
                elif difficulty == 'medium' or difficulty == '2':
                    difficulty = 2
                    enemy_HP = dinosaur_HP * 2 + random_stats * 2
                    enemy_attack = floor(dinosaur_attack / 2) - random_stats
                elif difficulty == 'hard' or difficulty == '3':
                    difficulty = 3
                    enemy_HP = (dinosaur_HP + random_stats) * 3
                    enemy_attack = floor(dinosaur_attack/1.5) - random_stats * 3
                else:
                    difficulty = 1
                    enemy_HP = floor(dinosaur_HP * 1.5)
                    enemy_attack = floor(dinosaur_attack / 3)

            print("")
            print("Searching for a battle...")
            time.sleep(random.randint(1, 5))
            print("Battle starting!")
            print("")
            print(f"Your enemy's health is {enemy_HP} and their attack is {enemy_attack}.")
            time.sleep(1)
            hexagon_point = 0
            enemy_hexagon_point = 0

            while battle_HP > 0 and enemy_HP > 0:
                attack_point = 0
                enemy_attack_point = 0
                shield_point = 0
                enemy_shield_point = 0

                print(f"Enemy used {enemy_hexagon_point} hexagon!") if enemy_hexagon_point > 0 else ()

                if hexagon_point == 0:
                    battle_option = get_input2('What would you like to do (attack (1), shield (2), hexagon (3))? ')
                    second_battle_option = ''
                    third_battle_option = ''
                elif hexagon_point == 1:
                    battle_option = get_input2('What would you like to do (attack (1), shield (2), hexagon (3))? ')
                    second_battle_option = get_input2('What else would you like to do (attack (1), '
                                                      'shield (2), hexagon (3))? ')
                    third_battle_option = ''
                else:
                    battle_option = get_input2('What would you like to do (attack (1), shield (2), hexagon (3))? ')
                    second_battle_option = get_input2('What else would you like to do (attack (1) , '
                                                      'shield (2) , hexagon (3))? ')
                    third_battle_option = get_input2('What else would you like to do (attack (1) , shield (2))? ')

                if enemy_hexagon_point == 0:
                    enemy_option = get_enemy_option(1, 4)
                    second_enemy_option = 0
                    third_enemy_option = 0
                elif enemy_hexagon_point == 1:
                    enemy_option = get_enemy_option(1, 4)
                    second_enemy_option = get_enemy_option(1, 4)
                    third_enemy_option = 0
                else:
                    if random.randint(1, 3) == 1:
                        enemy_option = get_enemy_option(1, 3)
                        second_enemy_option = get_enemy_option(1, 3)
                        third_enemy_option = get_enemy_option(1, 2)
                    else:
                        enemy_option = 1
                        second_enemy_option = 1
                        third_enemy_option = 1
                # 1 = attack, 2 = shield, 3 = hexagon

                if enemy_option == 4:
                    enemy_option = EnemyBattleOption.ATTACK

                if second_enemy_option == 4:
                    second_enemy_option = EnemyBattleOption.ATTACK
                hexagon_point = 0
                enemy_hexagon_point = 0

                attack_point += 1 if battle_option == BattleOption.ATTACK or battle_option == \
                                     BattleOption.ATTACK_NUMBER else 0
                attack_point += 1 if second_battle_option == BattleOption.ATTACK or second_battle_option == \
                                     BattleOption.ATTACK_NUMBER else 0
                attack_point += 1 if third_battle_option == BattleOption.ATTACK or third_battle_option == \
                                     BattleOption.ATTACK_NUMBER else 0

                enemy_attack_point += 1 if enemy_option == EnemyBattleOption.ATTACK else 0
                enemy_attack_point += 1 if second_battle_option == EnemyBattleOption.ATTACK else 0
                enemy_attack_point += 1 if third_enemy_option == EnemyBattleOption.ATTACK else 0

                shield_point += 1 if battle_option == BattleOption.SHIELD or battle_option == \
                                     BattleOption.SHIELD_NUMBER else 0
                shield_point += 1 if second_battle_option == BattleOption.SHIELD or second_battle_option == \
                                     BattleOption.SHIELD_NUMBER else 0
                shield_point += 1 if third_battle_option == BattleOption.SHIELD or third_battle_option == \
                                     BattleOption.SHIELD_NUMBER else 0

                enemy_shield_point += 1 if enemy_option == EnemyBattleOption.SHIELD else 0
                enemy_shield_point += 1 if second_enemy_option == EnemyBattleOption.SHIELD else 0
                enemy_shield_point += 1 if third_enemy_option == EnemyBattleOption.SHIELD else 0

                hexagon_point += 1 if battle_option == BattleOption.HEXAGON or battle_option == \
                                      BattleOption.HEXAGON_NUMBER else 0
                hexagon_point += 1 if second_battle_option == BattleOption.HEXAGON or second_battle_option == \
                                      BattleOption.HEXAGON_NUMBER else 0

                enemy_hexagon_point += 1 if enemy_option == EnemyBattleOption.HEXAGON else 0
                enemy_hexagon_point += 1 if second_enemy_option == EnemyBattleOption.HEXAGON else 0

                if attack_point >= 1 and enemy_shield_point == 0:
                    print(f"You used {attack_point} attack!")
                    print("Enemy used no shield!")
                    enemy_HP -= attack_point * dinosaur_attack
                    if enemy_HP < 0:
                        enemy_HP = 0
                    print(f"You did {dinosaur_attack * attack_point} damage!")
                    print(f"Enemy now has {enemy_HP} health.")
                    if enemy_HP == 0:
                        break

                elif attack_point >= 1 and enemy_shield_point >= 1:
                    if enemy_shield_point == 1:
                        print(f"You used {attack_point} attack but enemy used 1 shield.")
                    if enemy_shield_point == 2:
                        print(f"You used {attack_point} attack but enemy used 2 shields.")
                    attack_point -= enemy_shield_point
                    if attack_point < 0:
                        attack_point = 0
                    enemy_HP -= dinosaur_attack * attack_point
                    if enemy_HP < 0:
                        enemy_HP = 0
                    if attack_point == 0:
                        print("You did no damage.")
                    else:
                        print(f"You did {dinosaur_attack * attack_point} damage!")
                        print(f"Enemy now has {enemy_HP} health.")
                    if enemy_HP == 0:
                        break

                if enemy_attack_point >= 1 and shield_point == 0:
                    print(f"Enemy used {enemy_attack_point} attack.")
                    print("You used no shield.")
                    battle_HP -= enemy_attack_point * enemy_attack
                    if battle_HP < 0:
                        battle_HP = 0
                    print(f"Enemy did {enemy_attack_point * enemy_attack} damage.")
                    print(f"You now have {battle_HP} health.")

                elif enemy_attack_point >= 1 and shield_point >= 1:
                    if shield_point == 1:
                        print(f"Enemy used {enemy_attack_point} attack but you used 1 shield!")
                    if enemy_shield_point == 2:
                        print(f"Enemy used {enemy_attack_point} attack but you used 2 shields!")
                    enemy_attack_point -= shield_point
                    if enemy_attack_point < 0:
                        enemy_attack_point = 0
                    battle_HP -= enemy_attack * enemy_attack_point
                    if battle_HP < 0:
                        battle_HP = 0
                    if enemy_attack_point == 0:
                        print("Enemy did no damage!")
                    else:
                        print(f"Enemy did {enemy_attack * enemy_attack_point} damage.")
                        print(f"You now has {battle_HP} health.")

                total_battles += 1
                print("")

            if battle_HP == 0:
                defeats += 1
                print("Defeat")
            else:
                victories += 1
                print("Victory!")
                if difficulty == 1:
                    if random.randint(1, 3) == 3:
                        dinobuck_victories += 1
                        dinobucks += (10 + dinobuck_victories * 10)
                        print(f"You earned {9 + dinobuck_victories} dinobucks!")
                    else:
                        coin_victories += 1
                        coins += (100 + victories * 10)
                        print(f"You earned {90 + coin_victories * 10} coins!")
                elif difficulty == 2:
                    if random.randint(1, 3) == 3:
                        dinobuck_victories += 1
                        dinobucks += (10 + victories * 10)
                        print(f"You earned {13.5 + dinobuck_victories * 1.5} dinobucks!")
                    else:
                        coin_victories += 1
                        coins += (100 + victories * 10)
                        print(f"You earned {135 + coin_victories * 15} coins!")
                else:
                    if random.randint(1, 3) == 3:
                        dinobuck_victories += 1
                        dinobucks += (10 + victories * 10)
                        print(f"You earned {18 + dinobuck_victories * 2} dinobucks!")
                    else:
                        coin_victories += 1
                        coins += (100 + victories * 10)
                        print(f"You earned {180 + coin_victories * 20} coins!")

    else:
        print(f"You can't" + f' {option}')
