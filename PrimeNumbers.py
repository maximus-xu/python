number_list = [i for i in range(2, 100)]


def remove_multiple(number_list_parameter):
    first = number_list_parameter[0]
    result = []
    for i in number_list_parameter:
        if number_list_parameter[0] % first != 0:
            result.append(number_list_parameter[0])

    return result


for i in number_list:
    number_list = remove_multiple(number_list)
    print(number_list)
