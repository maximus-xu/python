import time


def countdown(t):
    while t:
        hours, secs = divmod(t, 3600)
        mins, secs = divmod(secs, 60)
        print(f'{hours:02d}:{mins:02d}:{secs:02d}', end="\r")
        time.sleep(1)
        t -= 1


t = int(input("Enter time: "))

countdown(t)
print("Time's up!")
