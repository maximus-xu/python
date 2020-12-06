

def frog_jump(steps):
    if steps < 1:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    return frog_jump(steps - 1) + frog_jump(steps - 2)


def frog_jump2(steps):
    if steps < 1:
        return 0
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2
    else:
        steps_list = [1, 2]
        while len(steps_list) < steps:
            steps_list.append(steps_list[-1] + steps_list[-2])
        return steps_list[-1]


print(frog_jump2(3))