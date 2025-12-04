joltages = []

with open("./2025/day3.txt", "r") as fp:
    lines = fp.readlines()
    
digits = 12 # just change to 2 for part 1
for bank in lines:
    bank = bank.strip()
    
    joltage = 0
    
    pos = -1
    for r in range(digits):
        max = -1
        start = pos + 1
        end = len(bank) - digits + r + 1
        for i, battery in enumerate(bank[start:end]):
            if int(battery) > max:
                max = int(battery)
                pos = start + i

        joltage = joltage * 10 + max 
            
    joltages.append(joltage)
    # print(joltage)

print(f"Sum of joltages: {sum(joltages)}")