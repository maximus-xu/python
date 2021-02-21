from importlib import resources
from utils.timeit import timeit


def get_data():
    if test_mode:
        return [10, 4, 6, 9, 0, 1, 7, 5, 13, 12, 6, 2, 8, 3, 17, 15, 59, 27, 16, 58, 19, 26, 47, 89, 55, 52, 92, 81, 35, 33]
    else:
        with resources.open_text("data", "numbers.csv") as data:
            lines = data.readlines()
            return [int(line) for line in lines]


def _spilt_list(x):
    middle = int(len(x)/2)
    a = x[:middle]
    b = x[middle:]
    return a, b


def _merge_list(a, b):
    index_a = 0
    index_b = 0
    return_list = []
    while len(return_list) != len(a) + len(b) and \
            index_a < len(a) and \
            index_b < len(b):

        if a[index_a] > b[index_b]:
            return_list.append(b[index_b])
            index_b += 1
        elif b[index_b] > a[index_a]:
            return_list.append(a[index_a])
            index_a += 1
        else:
            return_list += [a[index_a], a[index_a]]

            index_a += 1
            index_b += 1

    if index_b < len(b):
        return_list += b[index_b:]
    elif index_a < len(a):
        return_list += a[index_a:]

    return return_list


@timeit
def my_merge_sort(input_list):
    return merge_sort(input_list)


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    if len(input_list) == 2:
        return input_list if input_list[0] <= input_list[1] else \
                [input_list[1], input_list[0]]

    a, b = _spilt_list(input_list)
    a_sorted = merge_sort(a)
    b_sorted = merge_sort(b)
    return _merge_list(a_sorted, b_sorted)


@timeit
def bucket_sort(range_1, range_2, input_list):
    count = range_2 - range_1 + 1
    buckets = [0] * count
    output = []
    for i in input_list:
        buckets[i] += 1
    for i in range(count):
       output += [i] * buckets[i]
    return output

@timeit
def insertion_sort(input):
    output_list = []
    index = 0
    index_2 = 0
    valid = False

    while not valid:
        if len(output_list) == 0:
            output_list.append(input[index])
            index += 1

        else:
            if len(output_list) == len(input):
                valid = True
            else:
                while index < len(input):
                    number_1 = input[index]
                    number_2 = output_list[index_2]

                    if number_1 > number_2:
                        if index_2 + 1 == len(output_list):
                            output_list.append(number_1)
                            index += 1
                            break
                        else:
                            index_2 += 1
                    else:
                        output_list.insert(index_2, number_1)
                        index += 1
                        break
            index_2 = 0
    return output_list


test_mode = False
input = get_data()
print(insertion_sort(input))
print(bucket_sort(1, 10000, input))
print(my_merge_sort(input))