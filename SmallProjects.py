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
    if len(positions) == 8:
        for i in positions:
            line = ''
            for j in range(9):
                if j == i[1]:
                    line += 'Q '
                elif j != 0:
                    line += '. '
            print(line)
        print('')
        return

    row = positions[-1][0] + 1 if positions else 1
    possible = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in positions:
        possible.remove(i[1])
    for i in positions:
        diagonal = i[1]
        diagonal_2 = i[1]
        for i in range(row - i[0]):
            diagonal += 1
            diagonal_2 -= 1
        if diagonal in possible:
            possible.remove(diagonal)
        if diagonal_2 in possible:
            possible.remove(diagonal_2)
    for i in possible:
        eight_queens(positions + [[row, i]])

