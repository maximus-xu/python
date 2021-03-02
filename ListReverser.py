
def reverse(input):
    output = []
    for i in range(len(input)):
        output.append(input[-i-1])

    return output

