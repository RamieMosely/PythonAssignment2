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

def findOvertakeDay(plant1, plant2):
    if plant1.growthRate <= plant2.growthRate and plant1.height >= plant2.height:
        print(f"{plant1.name} starts taller and grows quicker or at the same rate as {plant2.name}.")
        print("There wont be any overtaking in growth!")
        return
    elif plant2.growthRate <= plant1.growthRate and plant2.height >= plant1.height:
        print(f"{plant2.name} starts taller and grows quicker or at the same rate as {plant1.name}.")
        print("There wont be any overtaking in growth!")
        return
    
    #overtake
    if plant1.growthRate > plant2.growthRate:
        faster = plant1
        slower = plant2
    else:
        faster = plant2
        slower = plant1

    days = (slower.height - faster.height) / (faster.growthRate - slower.growthRate)
    if days < 0:
        print(f"{faster.name} is taller than {slower.name}")
    else:
        days = int(days) + 1
        print(f"{faster.name} will be taller than {slower.name} on day {days}")
        print(f"Height of {faster.name}: {faster.getHeightAfterDays(days):.2f} cm")
        print(f"Height of {slower.name}: {slower.getHeightAfterDays(days):.2f} cm")

def changePlantInfo(plant1, plant2):
    while True:
        plantNum = input("Which plant would you like to modify?(1 or 2)\n")
        if plantNum == '1' or plantNum == '2':
            break
        print("Please enter either 1 or 2")

    name, height, growthRate = getPlantInfo()
    if plantNum == '1':
        return Plant(name, height, growthRate), plant2
    
    else:
        return plant1, Plant(name, height, growthRate)

