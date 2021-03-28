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
    total = 0
    i = 0
    while i < len(input):
        first, index = get_first_number(input[i:])
        total += first
        i += index
    return total


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
        return number, i+1 if i == len(input)-1 else i
    return -number, i+1 if i == len(input)-1 else i

