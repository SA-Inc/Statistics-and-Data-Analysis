from tabulate import tabulate

# 0 - case number
# 1 - price spread % (торговая наценка)
# 2 - purchase price $ (цена закупки)
# 3 - actual cargo turnover t (фактический грузооборот)
# 4 - warehouse rental cost $ (стоимость аренды складских помещений)
# 5 - salary $ (оплата труда АУП)
# 6 - handling cost $ (стоимость грузопереработки)
# 7 - aspect ratio (коэффициент  пропорциональности)

inputData = [
    [1, 5, 55, 1150, 450, 150, 280, 0.0012],
    [2, 6, 60, 1160, 500, 160, 300, 0.0016],
    [3, 7, 65, 1170, 560, 180, 320, 0.0018],
    [4, 8, 70, 1180, 700, 190, 340, 0.0021],
    [5, 9, 75, 1190, 560, 200, 360, 0.0026],
    [6, 10, 80, 1200, 400, 210, 380, 0.0032],
    [7, 11, 85, 1210, 700, 220, 400, 0.0011],
    [8, 12, 90, 1220, 720, 230, 420, 0.0014],
    [9, 13, 95, 1230, 730, 240, 440, 0.0015],
    [10, 14, 100, 1240, 750, 250, 460, 0.0017],
    [11, 15, 102, 1250, 770, 260, 480, 0.0021],
    [12, 16, 105, 1260, 800, 240, 500, 0.0023],
    [13, 17, 108, 1270, 900, 230, 520, 0.0027],
    [14, 18, 110, 1280, 550, 240, 540, 0.0029],
    [15, 19, 112, 1290, 600, 250, 560, 0.0011],
    [16, 20, 115, 1300, 700, 260, 580, 0.0013],
    [17, 19, 65, 1310, 800, 250, 600, 0.0019],
    [18, 18, 80, 1320, 900, 240, 620, 0.0024],
    [19, 17, 90, 1340, 800, 230, 640, 0.0034],
    [20, 16, 100, 1350, 550, 220, 660, 0.0021]
]

def getWarehouseTurnover(time, avgCargoCost):
    return avgCargoCost / time

def getCompanyIncome(cargoTurnover, purchasePrice, priceSpread):
    return (cargoTurnover * purchasePrice * priceSpread) / 100

def getHandlingCostPerTonne(handlingCost, cargoTurnover):
    return handlingCost / cargoTurnover

def getWarehouseBreakevenPoint(fixedCostAmount, purchasePrice, priceSpread, aspectRatio, handlingCostPerTonne):
    return fixedCostAmount / (purchasePrice * priceSpread - 100 * aspectRatio * purchasePrice - 100 * handlingCostPerTonne)

outputData = []

for case in inputData:
    companyIncome = round(getCompanyIncome(case[3], case[2], case[1]), 2)
    fixedCostAmount = round((case[4] + case[5]), 2)
    variableCostAmount = round(case[6], 2)
    warehouseIncome = round((companyIncome - (fixedCostAmount + variableCostAmount)), 2)
    handlingCostPerTonne = round(getHandlingCostPerTonne(case[6], case[3]), 2)
    warehouseBreakevenPoint = round(getWarehouseBreakevenPoint(fixedCostAmount, case[2], case[1], case[7], handlingCostPerTonne), 2)
    outputData.append(tuple((case[0], companyIncome, warehouseIncome, fixedCostAmount, variableCostAmount, handlingCostPerTonne, warehouseBreakevenPoint)))


print()
print("Input Data")
print(tabulate(inputData, tablefmt="presto", headers=["#", "Торговая наценка %", "Цена закупки $", "Грузооборот Т", "Аренды склада $", "Оплата труда $", "Грузопереработка $", "Коэффициент  пропорциональности"]))

print()
print("Output Data")
print(tabulate(outputData, tablefmt="presto", headers=["#", "Доход предприятия $", "Доход склада $", "Сумма постоянных издержек $", "Сумма переменных издержек $", "Стоимость грузопереработки/т $", "Точка безубыточности деятельности склада $"]))
