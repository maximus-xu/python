def reverse_string(input):
    output = ""
    index = -1
    count = len(input)
    while count != len(output):
        output += input[index]
        index -= 1

    return output


def parse_input_int(raw):
    try:
        return int(raw)
    except:
        return "error"


def parse_input_str(raw):
    try:
        return str(raw)
    except:
        return -1


def get_input(message):
    valid = False
    while not valid:
        raw_input = input(message)
        output = parse_input_int(raw_input)
        if output == "error":
            print("Please enter an integer value.")
        else:
            return output


def get_input2(message):
    valid = False
    while not valid:
        raw_input = input(message)
        output = parse_input_str(raw_input)
        if output == -1:
            print("Please enter a valid answer.")
        else:
            return output
