

def fence_painting(a, b, c, d):
    painted = set()
    for i in range(a, b):
        painted.add(i)
    for j in range(c, d):
        painted.add(j)
    return len(painted)


def mixing_milk(c1, m1, c2, m2, c3, m3):
    for i in range(33):

        m1 -= c2
        m2 += c2
        m2 += m1 if m1 < 0 else 0
        m1 = 0 if m1 < 0 else m1

        m2 -= c3
        m3 += c3
        m3 += m2 if m2 < 0 else 0
        m2 = 0 if m2 < 0 else m2

        m3 -= c1
        m1 += c1
        m1 += m3 if m3 < 0 else 0
        m3 = 0 if m3 < 0 else m3

    m1 -= c2
    m2 += c2
    m2 += m1 if m1 < 0 else 0
    m1 = 0 if m1 < 0 else m1

    return m1, m2, m3


def shell_game(n, swaps):
    cases = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for case in cases:
        for turn in swaps:
            return


def uddered_but_not_herd():
    cowphabet = input()
    word = input()
    count = 0
    current = 0
    dictionary = {}
    for i in range(len(cowphabet)):
        dictionary += cowphabet[i]
        dictionary[-1].v += i
    for i in word:
        current = dictionary[]


uddered_but_not_herd()