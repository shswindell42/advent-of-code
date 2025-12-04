joltages = []

with open("./2025/day3.txt", "r") as fp:
    lines = fp.readlines()
    
for bank in lines:
    bank = bank.strip()
    
    # max before last digit
    max = -1
    pos = -1
    for i, battery in enumerate(bank[:len(bank) - 1]):
        if int(battery) > max:
            max = int(battery)
            pos = i

    # max after max digit
    subsequent_max = -1
    for i, battery in enumerate(bank[pos+1:len(bank)]):
        if int(battery) > subsequent_max:
            subsequent_max = int(battery)
            
    joltage = max * 10 + subsequent_max
    joltages.append(joltage)
    print(joltage)

print(f"Sum of joltages: {sum(joltages)}")