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
