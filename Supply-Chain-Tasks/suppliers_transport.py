def renderCosts(type, rateOfFreight, wayStorageCost, insuranceCost, volume):
    totalRateOfFreight = volume * rateOfFreight
    totalWayStorageCost = volume * wayStorageCost
    totalInsuranceCost = volume * insuranceCost
    totalCost = totalRateOfFreight + totalWayStorageCost + totalInsuranceCost

    print(str(volume) + " m3 costs via " + type)
    print(str(volume) + " m3 Transportation Cost: " + str(round(totalRateOfFreight, 2)))
    print(str(volume) + " m3 Storage on Way Cost: " + str(round(totalWayStorageCost, 2)))
    print(str(volume) + " m3 Insurance Cost:      " + str(round(totalInsuranceCost, 2)))
    print(str(volume) + " m3 Total Cost:          " + str(round(totalCost, 2)))
    print()

    return totalCost

def getWayStorageCost(meterCubeCost, percentStorageRate, deliveryDays):
    return meterCubeCost * (percentStorageRate / 100) * (deliveryDays / 365)

def getInsuranceCost(meterCubeCost, extraAssemblyCosts, extraInsuranceDays):
    return meterCubeCost * (extraAssemblyCosts / 100) * (extraInsuranceDays / 365)

airRateOfFreight = 1454
airDeliveryDays = 10
airExtraInsuranceDays = 2
airPercentStorageRate = 3

waterRateOfFreight = 250
waterDeliveryDays = 50
waterExtraInsuranceDays = 14
waterPercentStorageRate = 7

extraAssemblyCosts = 15

costPerCubeMeter = 5000
volume = 1

waterWayStorageCost = getWayStorageCost(costPerCubeMeter, waterPercentStorageRate, waterDeliveryDays)
airWayStorageCost = getWayStorageCost(costPerCubeMeter, airPercentStorageRate, airDeliveryDays)
waterInsuranceCost = getInsuranceCost(costPerCubeMeter, extraAssemblyCosts, waterExtraInsuranceDays)
airInsuranceCost = getInsuranceCost(costPerCubeMeter, extraAssemblyCosts, airExtraInsuranceDays)

renderCosts("Water", waterRateOfFreight, waterWayStorageCost, waterInsuranceCost, volume)
renderCosts("Air", airRateOfFreight, airWayStorageCost, airInsuranceCost, volume)

volume = input("Entre volume(m3): ")

totalWaterCost = renderCosts("Water", waterRateOfFreight, waterWayStorageCost, waterInsuranceCost, int(volume))
totalAirCost = renderCosts("Air", airRateOfFreight, airWayStorageCost, airInsuranceCost, int(volume))

if (totalWaterCost > totalAirCost):
    print("Air Transport")
else:
    print("Water Transport")