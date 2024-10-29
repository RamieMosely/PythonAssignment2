#Ramie Mosely
#991332209
#Programming Assignment 2


class Plant:
    def __init__(self, name, height, growthRate):
        self.name = name
        self.height = height
        self.growthRate = growthRate

    def getHeightAfterDays(self, days):
        return self.height + (self.growthRate * days)

def getValidNumber(prompt, allowZero = True):
    while True:
        userInput = input(prompt)
        if userInput.replace(".", "", 1).isdigit():
            number = float(userInput)
            if not allowZero and number <= 0:
                print("Please enter a positive number!")
                continue
            if number < 0:
                print("Number cannot be negative!")
                continue
            return number
        print("Please enter a valid number!")

def getPlantInfo():
    name = input("Enter your plants name!\n")
    height = float(input("Enter the starting height!\n"))
    growthRate = float(input("Enter daily growth rate!\n"))
    return name, height, growthRate

def displayPlantInfo(plant1, plant2):
    print("\nPlant Information!")
    print(f"{plant1.name}")
    print(f"Current height: {plant1.height:.2f} cm")
    print(f"Daily growth rate: {plant1.growthRate:.2f} cm/day")
    print("------------------------")
    print(f"{plant2.name}")
    print(f"Current Height: {plant2.height:.2f} cm")
    print(f"Daily growth rate: {plant2.growthRate:.2f} cm/day")

def compareHeights(plant1, plant2):
    days = int(input("Enter number of days!\n"))
    height1 = plant1.getHeightAfterDays(days)
    height2 = plant2.getHeightAfterDays(days)

    print(f"{plant1.name}: {height1:.2f} cm")
    print(f"{plant2.name}: {height2:.2f} cm")
