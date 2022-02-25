# first_line = input().split(' ')
# k = int(first_line[0])
# n = int(first_line[1])
# x = []
# for i in range(n):
#     x.append(input())


def race(k, x, time):
    if k < 0:
        return
    if k == 0:
        return time

    times = []

    times += [race(k-x, x+1, time + 1)]
    times += [race(k-x, x-1, time + 1)]
    times += [race(k-x, x, time + 1)]

    smallest = times[0]
    for i in times:
        smallest = i if i < smallest else smallest

    return smallest


race(10, 1, 0)

