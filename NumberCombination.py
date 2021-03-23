

def number_combo(input, equation):
    if not input:
        total = 0
        for i in equation:
            total += i
        if total == 100:
            print(equation)
        return

    number_combo(input[1:], equation + [input[0]])
    number_combo(input[1:], equation + [-input[0]])
    if equation:
        number_combo(input[1:], equation + [input * 10 + input[0]] if equation[-1] > 0 else [input * 10 - input[0]])


number_combo([1, 2, 3, 4, 5, 6, 7, 8, 9], [])