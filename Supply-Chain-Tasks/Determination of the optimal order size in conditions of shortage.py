import math
from tabulate import tabulate

# 0 - case
# 1 - annualProductsDemand - D
# 2 - orderCosts - C1
# 3 - warehouseKeepingStockCosts - C2
# 4 - deficitLosses - С3

inputData = [
    [1, 1850, 210, 85, 350],
    [2, 3391, 242, 99, 387],
    [3, 3129, 236, 87, 408],
    [4, 2054, 242, 105, 354],
    [5, 2675, 232, 96, 418],
    [6, 2916, 247, 95, 353],
    [7, 2064, 212, 96, 404],
    [8, 2552, 215, 88, 354],
    [9, 2273, 222, 88, 364],
    [10, 2831, 291, 91, 407],
    [11, 2875, 235, 92, 368],
    [12, 2655, 241, 103, 374],
    [13, 2169, 262, 86, 395],
    [14, 2317, 223, 91, 398],
    [15, 2149, 249, 94, 385],
    [16, 3300, 228, 89, 391],
    [17, 3174, 245, 105, 358],
    [18, 2225, 279, 103, 378],
    [19, 2285, 270, 94, 357],
    [20, 2765, 214, 102, 377]
]

example = [0, 2200, 160, 150, 400]

def getOptimalOrderSize(annualProductsDemand, orderCosts, warehouseKeepingStockCosts):
    optimalOrderSize = math.sqrt((2 * annualProductsDemand * orderCosts) / warehouseKeepingStockCosts)
    return round(optimalOrderSize, 2)

def getOrderSizeWithDeficitLosses(warehouseKeepingStockCosts, deficitLosses):
    orderSizeWithDeficitLosses = math.sqrt((warehouseKeepingStockCosts + deficitLosses) / deficitLosses)
    return round(orderSizeWithDeficitLosses, 2)

def getStockWithDeficitLosses(warehouseKeepingStockCosts, deficitLosses):
    stockWithWithDeficitLosses = math.sqrt(deficitLosses / (warehouseKeepingStockCosts + deficitLosses))
    return round(stockWithWithDeficitLosses, 2)

def getMaxPossibleDeficit(orderSizeWithDeficitLosses, stockWithWithDeficitLosses):
    return orderSizeWithDeficitLosses - stockWithWithDeficitLosses

outputData = []

for row in inputData:
    qopt = getOptimalOrderSize(row[1], row[2], row[3])
    qd = getOrderSizeWithDeficitLosses(row[3], row[4])
    qn = getStockWithDeficitLosses(row[3], row[4])
    maxPossDif = getMaxPossibleDeficit(qd, qn)
    outputData.append(tuple((row[0], qopt, qd, qn, maxPossDif)))


print()
print("Input Data")
print(tabulate(inputData, tablefmt="presto", headers=["Case #", "Annual Products Demand", "Order Costs", "Warehouse Keeping Stock Costs", "Deficit Losses"]))

print()
print("Output Data")
print(tabulate(outputData, tablefmt="presto", headers=["Case #", "Optimal Order Size", "Order Size With Deficit Losses", "Stock With Deficit Lossess", "Max Possible Deficit"]))
