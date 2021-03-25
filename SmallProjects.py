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
    equation = ''
    for i in range(len(input)):
        if input[i] != ' ':
            equation += input[i]
    equation = equation.split('+')
    if type(equation) == str:
        equation = [equation]
    total = 0
    for i in range(len(equation)):
        try:
            equation[i] = int(equation[i])
        except:
            sub_total = 0
            equation[i] = equation[i].split('-')

            for j in range(len(equation[i])):
                if j == 0:
                    sub_total += int(equation[i][j])
                else:
                    sub_total -= int(equation[i][j])
            equation[i] = sub_total

    for i in equation:
        total += i

    print(total)


string_equation('')