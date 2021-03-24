def count(input, search_number):
    if len(input) == 0:
        return 0
    elif input[0] == search_number and input[-1] == search_number:
        return len(input)
    elif input[0] > search_number:
        return 0
    elif input[-1] < search_number:
        return 0

    middle = round(len(input ) /2)
    return count(input[:middle], search_number) + count(input[middle:], search_number)


print(count([1], 1))