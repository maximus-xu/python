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


def check_permutation_2(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    def count_items(a):
        map = {}
        for item in a:
            map[item] = map.get(item, 0) + 1
        return map

    return count_items(str_1) == count_items(str_2)


def palindrome_permutation_2(input):
    if not input:
        return True
    total_count = {}
    for letter in input:
        total_count[letter] = total_count.get(letter, 0) + 1

    odd_count = 0
    for v in total_count.values():
        odd_count += 1 if v % 2 == 1 else 0
        if odd_count == 2:
            return False
    return True


def get_index(book):
    def get_words(input):
        output = []
        word = ''
        for letter in input:
            if letter != ' ':
                word += letter
            else:
                try:
                    word = int(word)
                except:
                    output += [word]
                word = ''
        output += [word]
        return output

    index = {}
    for page in range(len(book)):
        book[page] = book[page].lower()
        for w in get_words(book[page]):
            if w not in index:
                index[w] = [page]
            elif index[w][-1] != page:
                index[w] += [page]

    return index


a = ['There are so many great short stories and so many poem',
     'that I was unable to trim the list to 100 titles',
     'so here are 160 Great Short Stories for you to enjoy.',
     'Click a button to find the best',
     'short stories from the authors below.'
    ]


def build_dic(input):
    dic = {}
    for i in input:
        dic[i] = 1 if i not in dic else dic[i] + 1
    return dic


def number_add(list_1, list_2, number):
    output = []
    dic = build_dic(list_1)
    for i in list_2:
        pair_value = number - i
        if pair_value in dic:
            output.append((i, pair_value))
            if dic[pair_value] > 1:
                dic[pair_value] -= 1
            else:
                dic.pop(pair_value)
    return output


def a(input_list):
    if len(input_list) == 1:
        return True
    steps = input_list[0]
    if steps == 0:
        return False
    for i in range(steps):
        a(input_list[steps:])


l1 = [3, 1, 2, 1, 1, 4]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(number_add(l1, l2, 9))