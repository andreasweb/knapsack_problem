class Food():
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.value/self.calories

    def __str__(self):
        return self.name + ": <" + str(self.value) + ", " + str(self.calories) + ">"

def buildMenu(names, values, calories):
    """
    names, values, calories lists of same length.
    names: list of strings.
    values and calories: lists of numbers.
    return: list of Foods.
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """
    Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers (sorts elements from best to worst, independently of the
    definition of "best" and "worst")
    """
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):  # iterate over each item
        if (totalValue + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

names = ["donut", "apple", "cake"]
values = [5, 10, 15]
calories = [300, 50, 3000]

foods = buildMenu(names, values, calories)


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print("Total value of items taken =", val)
    for item in taken:
        print(" ", item)

def testGreedys(foods, maxUnits):
    print("use greedy by value to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    print("use greedy by cost to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print("use greedy by density to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.density)


testGreedys(foods, 400)
