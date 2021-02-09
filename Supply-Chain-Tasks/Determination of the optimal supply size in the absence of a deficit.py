import math
from tabulate import tabulate

# case number
# implemented_products_per_day - Q
# goods_delivery_cost - C1
# warehouse_unit_storage_cost - C2
# gods_delivery_time_in_days - td
# demand_level - D
inputData = [
    [1, 100, 8, 13, 3, 5],
    [2, 110, 9, 12, 5, 5],
    [3, 120, 6, 15, 6, 6],
    [4, 130, 2, 18, 7, 9],
    [5, 140, 5, 19, 9, 7],
    [6, 150, 9, 24, 7, 8],
    [7, 160, 3, 23, 5, 6],
    [8, 170, 6, 10, 3, 2],
    [9, 180, 4, 16, 6, 3],
    [10, 190, 5, 14, 3, 5],
    [11, 210, 4, 16, 5, 9],
    [12, 220, 9, 18, 7, 8],
    [13, 230, 3, 19, 6, 2],
    [14, 240, 2, 20, 7, 3],
    [15, 250, 3, 21, 8, 7],
    [16, 260, 7, 25, 9, 9],
    [17, 270, 9, 26, 6, 6],
    [18, 280, 5, 28, 5, 2],
    [19, 290, 2, 23, 3, 5],
    [20, 300, 9, 24, 7, 5]
]

# Q - productUnitsNumber;
# T - storagePeriod;
# D - demandLevel;
# q - orderSize;
# q* - economicalOrderSize;
# q1 - orderPoint;
# td - orderDeliveryTime;
# n - orderNumberForStoragePeriod;
# C1 - oneOrderDeliveryCost;
# C2 - storageUnitCostPerTime;
# Сd - orderDeliveryCostForStoragePeriod;
# Сx - storageUnitsCostForStoragePeriod;
# С - logisticsSystemCostForStoragePeriod.

def getOptimalOrderSize(goodsDeliveryCost, warehouseUnitStorageCost, demandLevel):
    economicalOrderSize = math.sqrt((2 * goodsDeliveryCost * demandLevel) / warehouseUnitStorageCost)
    return round(economicalOrderSize)

def getOrderNumbersOverTime(demandLevel, orderSize):
    orderNumberForStoragePeriod = demandLevel / orderSize
    return round(orderNumberForStoragePeriod)

def getIntervalBetweenOrders(implementedProductsPerDay, orderNumberForStoragePeriod):
    interval = implementedProductsPerDay / orderNumberForStoragePeriod    
    return interval

def getOrderPoint(godsDeliveryTimeInDays, demandLevel, intervalBetweenOrders):
    orderPoint = godsDeliveryTimeInDays * (demandLevel / intervalBetweenOrders)
    return round(orderPoint, 2)

def getMinCost(goodsDeliveryCost, warehouseUnitStorageCost, demandLevel, optimalOrderSize):
    min = ((goodsDeliveryCost * demandLevel) / optimalOrderSize) + ((warehouseUnitStorageCost * optimalOrderSize) / 2)
    return round(min, 2)

outputData = []

for row in inputData:
    optimalOrderSize = getOptimalOrderSize(row[2], row[3], row[5])
    orderNumbersOverTime = getOrderNumbersOverTime(row[5], optimalOrderSize)
    intervalBetweenOrders = getIntervalBetweenOrders(row[1], orderNumbersOverTime)
    orderPoint = getOrderPoint(row[4], row[5], intervalBetweenOrders)
    minCost = getMinCost(row[2], row[3], row[5], optimalOrderSize)
    outputData.append(tuple((row[0], optimalOrderSize, orderNumbersOverTime, intervalBetweenOrders, orderPoint, minCost)))


print()
print("Input Data")
print(tabulate(inputData, tablefmt="presto", headers=["Case #", "Implemented Products per Day", "Goods Delivery Cost", "Warehouse Unit Storage Cost", "Gods Delivery Time in Days", "Demand Level"]))

print()
print("Output Data")
print(tabulate(outputData, tablefmt="presto", headers=["Case #", "Optimal Order Size", "Order Numbers Over Time", "Interval Between Orders", "Order Point", "Min Cost"]))