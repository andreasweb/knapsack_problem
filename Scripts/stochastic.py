# Implementing a random process

import random

def rollDie():
    return random.randint(1, 6)



def testRoll(n=10):
    result = ""
    for i in range(n):
        result += str(rollDie())
    print(result)


testRoll(10)