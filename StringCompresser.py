input_string = '123456789'


def method1():
    if len(input_string) == 0:
        exit(0)

    index = 0
    letter = input_string[index]
    count = 1
    output = ''

    for i in range(len(input_string)):
        index += 1
        if index == len(input_string):
            append = letter + str(count)
            output += append
            break
        if input_string[index] == letter:
            count += 1
        else:
            append = letter + str(count)
            output += append
            letter = input_string[index]
            count = 1

    print(output)


def find_compressed_string(string):
    if not string:
        return ""

    letter = string[0]
    count = 1
    for i in string[1:]:
        if i == letter:
            count += 1
        else:
            break

    return letter + str(count) + find_compressed_string(string[count:])

method1()
print(find_compressed_string(input_string))