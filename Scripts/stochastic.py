# Implementing a random processes

# Probabilities are always in the range between 0 and 1.
# If the probability of an event occurring is p, then the probability of the event not occurring is 1-p.
# When events are independent of each other, the probability of all the events occurring is equal to
# product of the probabilities of each of the events occurring.


import random

def rollDie():
    return random.randint(1, 6)



def testRoll(n=10):
    result = ""
    for i in range(n):
        result += str(rollDie())


    def runSim(goal, numTrials, txt):
        total = 0
        for i in range(numTrials):
            result = ''
            for j in range(len(goal)):
                result += str(rollDie())
            if result == goal:
                total += 1
        print('Actual probability of', txt, '=', round(1 / (6 ** len(goal)), 8))
        estProbability = round(total / numTrials, 8)
        print('Estimated Probability of', txt, '=', round(estProbability, 8))

    runSim('11111', 10000000, '11111')


testRoll(10)