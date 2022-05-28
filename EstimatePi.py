import random
repeat_int = 0


def generate_random():
    return random.random()


inside = 0
total = 10000000

while repeat_int <= total:
    x = generate_random()
    y = generate_random()
    if x*x + y*y <= 1:
        inside += 1
    repeat_int += 1
estimate = (inside/total) * 4
print(estimate)
pi = 3.141592653589793238462

print("{:1.2f}%".format((estimate-pi)/pi*100))