import time
import random


def generate():
    while True:
        yield random.randint(1,6), random.randint(1,6)
        time.sleep(.1)


c = 1
for i, j in generate():
    print(f'Try: {c}', end='\r')
    if i==6 and j==6:
        print(f"Found: {c}")
        break
    c += 1
 
