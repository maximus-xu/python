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

coin_set = [1, 5, 10, 25]
print(find_coin_count(100, coin_set, []))