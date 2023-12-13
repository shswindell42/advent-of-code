
def validCheck(char: str) -> bool:
    return char != '.' and not char.isdigit()


engine: list[list[str]] = []
engineNumbers: list[list[int]] = []

with open('day3.txt', 'r') as fp:
    for line in fp.readlines():
        engine.append([*(line.strip())])
        engineNumbers.append([0] * len(line))

partNumberSum = 0
partNumber = 0
isValid = False

for lineIdx, line in enumerate(engine):
    for charIdx, char in enumerate(line):
        if not char.isdigit():
            # reset
            partNumberSum += partNumber if isValid else 0

            # record number in engineNumbers
            if partNumber:
                for d in range(len(str(partNumber))):
                    engineNumbers[lineIdx][charIdx - 1 - d] = partNumber

            partNumber = 0
            isValid = False
        else:
            partNumber = partNumber * 10 + int(char)

            # check if valid
            if not isValid:
                if lineIdx > 0:
                    # look up
                    topChar = engine[lineIdx - 1][charIdx] 
                    isValid = validCheck(topChar) or isValid
                
                    # look top right
                    if charIdx < len(line) - 1:
                        topRightChar = engine[lineIdx - 1][charIdx + 1]
                        isValid = validCheck(topRightChar) or isValid
                            
                    # look top left
                    if charIdx > 0:
                        topLeftChar = engine[lineIdx - 1][charIdx - 1]
                        isValid = validCheck(topLeftChar) or isValid

                if lineIdx < len(engine) - 1:
                    # look down
                    bottomChar = engine[lineIdx + 1][charIdx]
                    isValid = validCheck(bottomChar) or isValid

                    # look bottom right
                    if charIdx < len(line) - 1:
                        bottomRightChar = engine[lineIdx + 1][charIdx + 1]
                        isValid = validCheck(bottomRightChar) or isValid

                    # look bottom left
                    if charIdx > 0:
                        bottomLeftChar = engine[lineIdx + 1][charIdx - 1]
                        isValid = validCheck(bottomLeftChar) or isValid

                # look left
                if charIdx > 0:
                    leftChar = engine[lineIdx][charIdx - 1]
                    isValid = validCheck(leftChar) or isValid

                # look right
                if charIdx < len(line) - 1:
                    rightChar = engine[lineIdx][charIdx + 1]
                    isValid = validCheck(rightChar) or isValid

        if charIdx == len(line) - 1:
            # reset
            partNumberSum += partNumber if isValid else 0

            # record number in engineNumbers
            if partNumber:
                for d in range(len(str(partNumber))):
                    engineNumbers[lineIdx][charIdx - 1 - d] = partNumber

            partNumber = 0
            isValid = False

print(partNumberSum)

# second pass to find the *
# needs to be a second pass because the 
# engineNumber map needs to be built
gearRatioSum = 0
for lineIdx, line in enumerate(engine):
    for charIdx, char in enumerate(line):
        if char == '*':
            # find the two nearby numbers
            top = engineNumbers[lineIdx - 1][charIdx]
            topLeft = engineNumbers[lineIdx - 1][charIdx - 1]
            topRight = engineNumbers[lineIdx - 1][charIdx + 1]
            left = engineNumbers[lineIdx][charIdx - 1]
            right = engineNumbers[lineIdx][charIdx + 1]
            bottom = engineNumbers[lineIdx + 1][charIdx]
            bottomLeft = engineNumbers[lineIdx + 1][charIdx - 1]
            bottomRight = engineNumbers[lineIdx + 1][charIdx + 1]
            
            distinct = set([top, topLeft, topRight, left, right, bottom, bottomLeft, bottomRight])
            distinct.discard(0)
            if len(distinct) == 2:
                first, second = distinct
                gearRatioSum += first * second

print(gearRatioSum)