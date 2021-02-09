import operator

def calcScore(currentArrtibute, maxAttribute, minAttribute, maxScore = 10, minScore = 1):
    return round(1 + (abs(currentArrtibute - minAttribute) / (maxAttribute - minAttribute)) * (maxScore - minScore), 2)

class Supplier:
    def __init__(self, name, price, distance, volume, security, experience):
        self.name = name # string
        self.price = price # number
        self.distance = distance # number
        self.volume = volume # number
        self.security = security # boolean
        self.experience = experience # number
        self.totalScore = None # null

suppliers = []

suppliers.append(Supplier("Supplier 1", 5, 158, 10, True, 10))
suppliers.append(Supplier("Supplier 2", 5.4, 163, 20, False, 5))
suppliers.append(Supplier("Supplier 3", 5.3, 182, 10, True, 15))
suppliers.append(Supplier("Supplier 4", 4.9, 210, 15, False, 5))

minSuppliersPrice = min(suppliers, key = operator.attrgetter('price'))
maxSuppliersPrice = max(suppliers, key = operator.attrgetter('price'))

minSuppliersDistance = min(suppliers, key = operator.attrgetter('distance'))
maxSuppliersDistance = max(suppliers, key = operator.attrgetter('distance'))

minSuppliersVolume = min(suppliers, key = operator.attrgetter('volume'))
maxSuppliersVolume = max(suppliers, key = operator.attrgetter('volume'))

minSuppliersExperience = min(suppliers, key = operator.attrgetter('experience'))
maxSuppliersExperience = max(suppliers, key = operator.attrgetter('experience'))

for supplier in suppliers:
    supplier.totalScore = calcScore(supplier.price, maxSuppliersPrice.price, minSuppliersPrice.price) + calcScore(supplier.distance, maxSuppliersDistance.distance, minSuppliersDistance.distance) + calcScore(supplier.volume, maxSuppliersVolume.volume, minSuppliersVolume.volume) + (1 if supplier.security else 0) + calcScore(supplier.experience, maxSuppliersExperience.experience, minSuppliersExperience.experience)

suppliers.sort(key = lambda supplier: supplier.totalScore, reverse = True)

print("Total Score:")
for supplier in suppliers:
    print(supplier.name + ": " + str(supplier.totalScore))
