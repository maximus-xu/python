def string_equation_2(input):
    def get_first_number(input):
        digits = [c for c in "0123456789"]
        negative = 0
        number = 0
        for i in range(len(input)):
            if input[i] == '-':
                negative += 1
            elif input[i] in digits:
                index = i
                break

        for i in range(index, len(input)):
            if input[i] in digits:
                number *= 10
                number += int(input[i])
            else:
                break

        if negative % 2 == 0:
            return number, i + 1 if i == len(input) - 1 else i
        return -number, i + 1 if i == len(input) - 1 else i

    total = 0
    i = 0
    while i < len(input):
        first, index = get_first_number(input[i:])
        total += first
        i += index
    print(total)


def check_permutation_2(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    str_1_count = {}
    str_2_count = {}
    for item in str_1:
        str_1_count[item] = str_1_count.get(item, 0) + 1

    for item in str_2:
        str_2_count[item] = str_2_count.get(item, 0) + 1

    return str_1_count == str_2_count


def palindrome_permutation_2(input):
    if not input:
        return True
    total_count = {}
    for letter in input:
        total_count[letter] = total_count.get(letter, 0) + 1

    odd_count = 0
    for v in total_count.values():
        odd_count += 1 if v % 2 == 1 else 0
        if odd_count == 2:
            return False
    return True


print(check_permutation_2('', ''))
