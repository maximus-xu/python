
def reverse(input):
    output = []
    for i in range(len(input)):
        output.append(input[-i-1])

    return output


def recursion_reverse(input):
    if not input:
        return []
    return recursion_reverse(input[1:]) + input[0:1]


def abc(input):
    return (input - 2)*180/input


print(abc(9000000000000000000000000000000000000000000000))