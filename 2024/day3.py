import re

total = 0

mul_enabled = True
with open("./2024/day3.txt", "r") as fp:
    for line in fp.readlines():
        mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
        
        matches = re.finditer(mul_pattern, line)
        for match in matches:
            command = match.group(0)
            
            if command == "do()":
                mul_enabled = True
            elif command == "don't()":
                mul_enabled = False
            else:
                if mul_enabled:
                    lhs = int(match.group(1))
                    rhs = int(match.group(2))
                    total += lhs * rhs
            
print(total)