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
