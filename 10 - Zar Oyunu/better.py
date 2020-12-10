import time
import random


def generate():
    while True:
        yield random.randint(1,6), random.randint(1,6)
        time.sleep(.1)


c = 1
for i, j in generate():
    if i == j == 6:
        print(f"Found: {c}")
        break
    else:
        print(f'Try: {c}', end='\r')
        c += 1
