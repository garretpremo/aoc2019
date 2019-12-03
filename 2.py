
if __name__ == '__main__':
    file = open('input2.txt')

    intCodes = file.read().split(',')

    intCodes[1] = 12
    intCodes[2] = 2

    index = 0

    while True:
        opcode = int(intCodes[index])
        
        if opcode == 1 or opcode == 2:
            firstNumber = int( intCodes[ int( intCodes[ index + 1 ] ) ] )
            secondNumber = int( intCodes[ int( intCodes[ index + 2 ] ) ] )
            replacementIndex = int( intCodes[ index + 3 ] )

            if opcode == 1:
                intCodes[replacementIndex] = firstNumber + secondNumber
            elif opcode == 2:
                intCodes[replacementIndex] = firstNumber * secondNumber
        elif opcode == 99:
            break
        else:
            print('Error')

        index += 4

    print(intCodes[0])
