from math import floor

if __name__ == '__main__':
    file = open('input.txt')
    
    masses = file.read().split()
    totalFuel = 0
    print('opened file')

    for mass in masses:
        totalFuel += floor(int(mass) / 3) - 2

    print(totalFuel)
    file.close()
