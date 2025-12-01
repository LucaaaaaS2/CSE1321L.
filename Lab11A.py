class BuildingBlueprint:
    def __init__(self, stories=10, apartment=20, rate=1.0):
        self.stories = stories
        self.apartment = apartment
        self.rate = rate

        if self.rate == 1.0:
            self.full = True
        else:
            self.full = False

    def update(self, newRate):
        self.rate = newRate

        if self.rate == 1.0:
            self.full = True
        else:
            self.full = False

buildingOne = BuildingBlueprint()
buildingTwo = BuildingBlueprint(30,30,.75)

print("Year 2025:")
print(f"Building 1 has {buildingOne.stories} floors, {buildingOne.apartment} apartments, and is {int(buildingOne.rate * 100)}% occupied. Full? {buildingOne.full} ")
print(f"Building 2 has {buildingTwo.stories} floors, {buildingTwo.apartment} apartments, and is {int(buildingTwo.rate * 100)}% occupied. Full? {buildingTwo.full} ")
print()
print("Many years passed")
print()
buildingOne.update(0.0)
buildingTwo.update(1.0)

print(f"Building 1 has {buildingOne.stories} floors, {buildingOne.apartment} apartments, and is {int(buildingOne.rate * 100)}% occupied. Full? {buildingOne.full} ")
print(f"Building 2 has {buildingTwo.stories} floors, {buildingTwo.apartment} apartments, and is {int(buildingTwo.rate * 100)}% occupied. Full? {buildingTwo.full} ")
print("Looks like people prefer taller buildings.")

