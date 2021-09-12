

def palindrome_problem():
    input_str = str(input("Enter: "))
    reversed_input = reverse_string(input_str)
    print(reversed_input == input_str)


def palindrome_recursion(input):
    if len(input) <= 1:
        return True
    return input[0] == input[-1] and palindrome_recursion(input[1:-1])


def a(steps):
    if steps < 0:
        return 0
    if steps == 0:
        return 1
    return a(steps-1) + a(steps-2) + a(steps-3)

sum = 0
for i in range(100000):
    if 10000 <= i <= 99999:
        if palindrome_recursion(str(i)):
            sum += i
print(sum)