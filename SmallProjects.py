import unittest


def parenthesis(left, right, input):
    if right == 0:
        print(input)
        return

    if left == right:
        parenthesis(left - 1, right, input + '(')
    elif left == 0:
        parenthesis(0, right - 1, input + ')')
    else:
        parenthesis(left - 1, right, input + '(')
        parenthesis(left, right - 1, input + ')')


def number_combo(input, output):
    if not input:
        total = 0
        for i in output:
            total += i
        if total == 100:
            print(output)
        return

    short = input[1:]

    if not output:
        number_combo(short, [input[0]])
        number_combo(short, [-input[0]])
    else:
        number_combo(short, output + [input[0]])
        number_combo(short, output + [-input[0]])
        number_combo(short, output[:-1] + [output[-1] * 10 + input[0]] if output[-1] > 0 else
        [output[-1] * 10] + [-input[0]])


def string_equation(input):
    equation = []

    for i in range(len(input)):
        if input[i] != ' ':
            equation += [input[i]]
    total = 0

    for i in range(len(equation)):
        try:
            equation[i] = int(equation[i])
        except:
            equation[i] = equation[i].split('-')
            for j in range(len(equation[i])):
                total += int(equation[i][j]) if j == 0 else -int(equation[i][j])
            equation[i] = 0

    for i in equation:
        total += i

    print(total)


def eight_queens(positions):
    BOARD_SIZE = 8

    def print_queens(positions):
        for p in positions:
            line = ''
            for col in range(BOARD_SIZE):
                if col == p:
                    line += 'Q  '
                else:
                    line += '.  '
            print(line)
        print()
        return

    if len(positions) == BOARD_SIZE:
        return print_queens(positions)

    possible = list(range(BOARD_SIZE))

    def remove_column():
        for p in positions:
            possible.remove(p)

    def remove_diagonal():
        row = len(positions)
        for i, p in enumerate(positions):
            row_diff = row - i
            diagonal_right = p + row_diff
            diagonal_left = p - row_diff

            if diagonal_right in possible:
                possible.remove(diagonal_right)
            if diagonal_left in possible:
                possible.remove(diagonal_left)

    remove_column()
    remove_diagonal()
    for p in possible:
        eight_queens(positions + [p])


def restriction_perm(input, restrictions, used):
    global restriction_perm_result

    def can_use(input, restrictions, used):
        if input in used:
            return False
        for restriction in restrictions:
            if input == restriction[1] and restriction[0] not in used:
                return False
        return True

    if len(input) == len(used):
        restriction_perm_result += [used]
        return
    for i in range(len(input)):
        if can_use(input[i], restrictions, used):
            restriction_perm(input, restrictions, used + [input[i]])


def letter_card(boxes, word, used):
    def can_use(box, used_boxes, letter):
        return box not in used_boxes and letter in box

    if not word:
        return True

    for i in range(len(boxes)):
        if can_use(boxes[i], used, word[0]):
            if letter_card(boxes, word[1:], used + [boxes[i]]):
                return True
    return False


def fences(map, start):
    def is_house(houses, house, visited):
        x = house[0]
        y = house[1]
        return 0 <= x < len(map) and \
            0 <= y < len(map[0]) and \
            house not in visited and \
            houses[x][y] == 1

    def visit(houses, house, visited):
        if not is_house(houses, house, visited):
            return 0
        total = 0
        x = house[0]
        y = house[1]
        visited += [house]
        total += 1 if is_house(houses, (x + 1, y), visited) else 0
        total += 1 if is_house(houses, (x, y + 1), visited) else 0

        for d in directions:
            total += visit(houses, (x + d[0], y + d[1]), visited)
        return total

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = []
    print(visit(map, start, visited))


def check_permutation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    if not str_1:
        return True
    letter = str_1[0]
    if letter in str_2:
        str_1.remove(letter)
        str_2.remove(letter)
        return check_permutation(str_1, str_2)
    return False


def palindrome_permutation(input):
    if not input:
        return True
    odd_count = 0
    letters = []
    for character in input:
        letter_count = 0
        if character not in letters:
            for item in input:
                if item == character:
                    letter_count += 1
            if letter_count % 2 != 0:
                odd_count += 1
        letters.append(character)
    return odd_count < 2


def pairs_with_sum(input, number):
    sums = []
    for i in range(len(input)):
        for j in range(len(input)):
            sums += [f'{input[i]} + {input[j]}'] if input[i] + input[j] == number and j > i else []
    return sums


def build_number_dictionary(input):
    numbers = {}
    for num in input:
        numbers[num] = numbers.get(num, 0) + 1
    return numbers


def pairs_with_sum2(input, number):

    def print_equation(matching):
        print(f'{num} + {matching}')

    def subtract_from_count(matching):
        numbers[num] = numbers.get(num) - 1
        numbers[matching] = numbers.get(matching) - 1

    def find_matching():
        matching = number - num
        if numbers.get(matching, 0) >= 1:
            if num != matching or (num == matching and numbers.get(num) > 1):
                print_equation()
                subtract_from_count(matching)

    numbers = build_number_dictionary(input)

    for num in input:
        find_matching(num)


# pairs_with_sum2([1, 2, 2, 2, 2, 3, 4, 5, 6], 4)


class ProjectTest(unittest.TestCase):

    def test_build_number_dictionary(self):
        numbers = [1, 2, 2, 4, 3, 5, 4, 2]
        number_dict = build_number_dictionary(numbers)
        self.assertEqual(number_dict, {1: 1, 2: 3, 3: 1, 4: 2, 5: 1})


if __name__ == '__main__':
    unittest.main()