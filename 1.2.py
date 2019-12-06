from math import floor

def getFuelsFuel(fuel):
    fuelsFuel = floor(int(fuel) / 3) - 2

    if (fuelsFuel <= 0):
        return 0
    else:
        return fuelsFuel + getFuelsFuel(fuelsFuel)

if __name__ == '__main__':
    inputFile = open('input1.txt')
    
    masses = inputFile.read().split()

    inputFile.close()

    totalFuel = 0

    for mass in masses:
        totalFuel += getFuelsFuel(int(mass))

    print(totalFuel)
