def validPassword(word):
    word = str(word)
    numbers = set(word)
    previous = 0

    for i in range(len(word)):
        number = int(word[i])

        if number < previous:
            return False
        
        previous = number
    
    return len(numbers) != len(word)

def adjustCurrent(word):
    word = str(word)
    foundLow = False
    previous = 0

    for i in range(len(word)):
        number = int(word[i])

        if foundLow:
            word[i] = str(previous)
        elif number < previous:
            word[i] = str(previous)
            foundLow = True

    return int(word)

if __name__ == '__main__':

    f = open('input4.txt')

    passwordRange = f.read().split('-')

    f.close()

    begin = int(passwordRange[0])
    end = int(passwordRange[1])

    current = begin

    answer = 0

    while current < end:
        if validPassword(current):
            answer += 1
        else:
            current = adjustCurrent(current)
        current += 1

    print(answer)