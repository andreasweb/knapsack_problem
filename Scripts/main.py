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
    keyFunction maps elements of items to numbers
    """
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalValue + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)


names = ["donut", "apple", "cake"]
values = [5, 10, 15]
calories = [300, 50, 3000]

m = buildMenu(names, values, calories)
