from food import buildMenu, testGreedys


names = ["donut", "apple", "cake", "banana", "pizza", "burger"]
values = [70, 30, 60, 20, 90, 100]
calories = [150, 50, 300, 70, 900, 500]

foods = buildMenu(names, values, calories)

testGreedys(foods, 300)
