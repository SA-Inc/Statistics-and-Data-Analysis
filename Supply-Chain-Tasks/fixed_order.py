import math
import matplotlib
import matplotlib.pyplot as plt

consumptionPerDay = [25, 26, 36, 45, 52, 36, 15, 36, 41, 33, 41, 56, 36, 61, 36, 25, 23, 27, 29, 32, 25, 26, 35, 41, 44, 46, 38, 39, 46, 32]

# ежедневный средний расход - d3
avgConsumptionPerMonth = round(sum(consumptionPerDay) / len(consumptionPerDay))

checkPeriodInDays = 3 # R
delayBetweenOrderRequestAndOrderProcessingInDays = 2 # L
currentProductUnits = 550 # Qfac
productsSafetyStockUnits = 150 # Qsafe
checkoutCosts = 2800 # C1
warehouseStockKeepingCostsPerDay = 5 # C2

optimalOrderSize = round(math.sqrt((2 * checkoutCosts * avgConsumptionPerMonth) / warehouseStockKeepingCostsPerDay))

print()
print('Оптимальный размер заказа: {} единиц товара'.format(optimalOrderSize))

daysCounter = 0
i = 0

print()

# данные для графика
days = []
remainUnitsByDays = []

while (i < 50):
    remainUnitsWhileCheckPeriod = currentProductUnits - checkPeriodInDays * avgConsumptionPerMonth
    currentProductUnits = remainUnitsWhileCheckPeriod
    daysCounter += checkPeriodInDays

    days.append(daysCounter)
    remainUnitsByDays.append(remainUnitsWhileCheckPeriod)
    print('Итерация: {}, день: {}, оставшиеся количество единиц товара в период проверки: {} единиц товара'.format(i, daysCounter, remainUnitsWhileCheckPeriod))

    remainUnitsWhileOrderRequestPeriod = currentProductUnits - delayBetweenOrderRequestAndOrderProcessingInDays * avgConsumptionPerMonth
    currentProductUnits = remainUnitsWhileOrderRequestPeriod
    daysCounter += delayBetweenOrderRequestAndOrderProcessingInDays

    days.append(daysCounter)
    remainUnitsByDays.append(remainUnitsWhileOrderRequestPeriod)
    print('Итерация: {}, день: {}, оставшиеся количество единиц товара в период оформления заказа: {} единиц товара'.format(i, daysCounter, remainUnitsWhileOrderRequestPeriod))


    if (currentProductUnits < productsSafetyStockUnits):
        currentProductUnits += optimalOrderSize
        print('Делаем заказ на {} итерации, {} дне. Единиц товара после заказа: {}'.format(i, daysCounter, currentProductUnits))

    i += 1

print()


fig, ax = plt.subplots()
ax.plot(days, remainUnitsByDays)
ax.set(xlabel='День', ylabel='Количество единиц товара', title='Система фиксированного заказа')
ax.grid()
plt.axhline(y = productsSafetyStockUnits, color='r', linestyle='-')
plt.show()