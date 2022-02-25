T = int(input())
dice = []
for i in range(T):
    dice += [input()]


def compile_die(die):
    return [int(i) for i in die.split(' ')]


def beat_score(a, b):
    score = 0
    for i in a:
        for j in b:
            if i > j:
                score += 1
    return score


def can_beat(a, b):
    score = beat_score(a, b)
    if score > 8:
        return True
    return score > beat_score(b, a)


def get_all():
    c = []
    for i in range(1,11):
        for j in range(1,11):
            for k in range(1,11):
                for l in range(1,11):
                    c += [[i,j,k,l]]
    return c


all = get_all()


def find(a, b):
    global all
    for c in all:
        if can_beat(b, c):
            if can_beat(c, a):
                return "yes"
    return "no"


for i in range(T):
    compiled = compile_die(dice[i])
    a = compiled[:4]
    b = compiled[4:]
    if can_beat(a, b):
        print(find(a, b))
    elif can_beat(b, a):
        print(find(b, a))
    else:
        print('no')