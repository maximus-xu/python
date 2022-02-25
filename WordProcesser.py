def method_1():
    with open("word.in") as f:
        lines = f.read()

    print(lines)


def method_2():
    with open("word.in") as f:
        lines = f.readlines()
        output = []
        for line in lines:
            output += [line.strip('\n')]
        return output


def method_3():
    with open("word.in") as f:
        line = f.readline()

        while line:
            print(line.strip('\n'))
            line = f.readline()


output_file = open("word.out", "w")

lines = method_2()
format = lines[0].split(' ')
K = int(format[1])
essay = lines[1].split(' ')
line = ''

characters = 0
for word in essay:
    if characters + len(word) > K:
        output_file.writelines(line[:-1] + "\n")
        characters = 0
        line = ''
    line += f"{word} "
    characters += len(word)

output_file.writelines(line + "\n")
output_file.close()
