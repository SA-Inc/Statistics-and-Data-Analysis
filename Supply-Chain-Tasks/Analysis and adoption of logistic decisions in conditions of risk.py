import math
from tabulate import tabulate

eventsProbability1 = [
    [4000.00, 0.15],
    [3700.00, 0.14],
    [6892.00, 0.26],
    [6100.00, 0.23],
    [5800.00, 0.22]
]

eventsProbability2 = [
    [5000.00, 0.19],
    [4500.00, 0.17],
    [5900.00, 0.22],
    [4500.00, 0.17],
    [7000.00, 0.25]
]

def mathematicalExpectation(eventsList):
    mathExpect = 0

    for event in eventsList:
        mathExpect += event[0] * event[1]

    return mathExpect

def variance(eventsList, mathExpect):
    varianceResult = 0

    for event in eventsList:
        varianceResult += (event[0] ** 2) * event[1]

    return varianceResult - (mathExpect ** 2)

def standardDeviation(variance):
    return math.sqrt(variance)

outputData = []

me1 = mathematicalExpectation(eventsProbability1)
v1 = variance(eventsProbability1, me1)
sd1 = standardDeviation(v1)

me2 = mathematicalExpectation(eventsProbability2)
v2 = variance(eventsProbability2, me2)
sd2 = standardDeviation(v2)

outputData.append(tuple((1, me1, v1, sd1)))
outputData.append(tuple((2, me2, v2, sd2)))

print()
print('Проект 1')
print(tabulate(eventsProbability1, floatfmt=".2f", tablefmt="presto", headers=["Доход", "Вероятность"]))
print()
print('Проект 2')
print(tabulate(eventsProbability2, floatfmt=".2f", tablefmt="presto", headers=["Доход", "Вероятность"]))
print()
print('Показатель расчета: доход проекта')
print(tabulate(outputData, floatfmt=".2f", tablefmt="presto", headers=["Проект", "Мат. ожидание", "Дисперсия", "Стандартное отклонение"]))
print()