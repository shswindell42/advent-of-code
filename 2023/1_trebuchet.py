import regex

path = "./adventofcode.com_2023_day_1_input.txt"
calibrationSum = 0

digitStrings = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

with open(path, 'r') as fp:
    for line in fp.readlines():            
        calibration = 0
        firstDigit = 0
        lastDigit = 0
        digitFound = False
        for lineIdx, c in enumerate(line):
            if c.isnumeric():
                if not digitFound:
                    firstDigit = int(c)
                    digitFound = True
                lastDigit = int(c)
            else:
                # transform the string convert digit words to digits
                for i, d in enumerate(digitStrings):
                    if line[lineIdx:lineIdx + len(d)] == d:
                        if not digitFound:
                            firstDigit = i + 1
                            digitFound = True
                        lastDigit = i + 1
        
        calibration = firstDigit * 10 + lastDigit
        print(f"{line.strip()} -> {calibration}")

        calibrationSum += calibration

print(f"Calibration Sum is {calibrationSum}")