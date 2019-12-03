import math

def runIntCodes(intCodes, noun, verb):
    index = 0

    intCodes[1] = noun
    intCodes[2] = verb

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

    return intCodes[0]

if __name__ == '__main__':
    file = open('input2.txt')

    intCodes = file.read().split(',')

    finalAnswer = 19690720

    baseAnswer = runIntCodes(intCodes.copy(), 0, 0)
    nounOffset = runIntCodes(intCodes.copy(), 1, 0) - baseAnswer
    verbOffset = runIntCodes(intCodes.copy(), 0, 1) - baseAnswer
    nounAndVerbOffset = runIntCodes(intCodes.copy(), 1, 1) - baseAnswer

    assert(baseAnswer + nounAndVerbOffset == baseAnswer + nounOffset + verbOffset)

    offsetFinalAnswer = finalAnswer - baseAnswer

    noun = 0
    verb = 0

    if nounOffset > verbOffset:
        noun = math.floor(offsetFinalAnswer / nounOffset)
        answerWithNoun = runIntCodes(intCodes.copy(), noun, 0)

        verb = math.floor((finalAnswer - answerWithNoun) / verbOffset)
    else:
        verb = math.floor(offsetFinalAnswer / verbOffset)
        answerWithVerb = runIntCodes(intCodes.copy(), 0, verb)

        noun = math.floor((finalAnswer - answerWithVerb) / nounOffset)
    
    print(((100 * noun) + verb))