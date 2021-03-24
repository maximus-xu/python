
def reverse(input):
    output = []
    for i in range(len(input)):
        output.append(input[-i-1])

    return output


def recursion_reverse(input):
    if not input:
        return []
    return recursion_reverse(input[1:]) + input[0:1]

