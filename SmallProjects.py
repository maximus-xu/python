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


restriction_perm_result = []


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
            restriction_perm(input, restrictions, used+[input[i]])


