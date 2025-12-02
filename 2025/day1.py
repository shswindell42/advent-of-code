zero_count = 0
passed_zero_count = 0
current = 50

with open("./2025/day1.txt", mode="r") as fp:
    for line in fp.readlines():
        direction = -1 if line[0] == "L" else 1
        length = int(line[1:])

        # passed zero for each 100
        passed_zero_count += length // 100
        length = length % 100
        
        previous = current
        change = (current + (length * direction))
        current = change % 100
        
        if current == 0:
            zero_count += 1
        elif direction == -1 and change < 0 and previous != 0: 
            passed_zero_count += 1
        elif direction == 1 and change > 100 and previous != 0:
            passed_zero_count += 1
            
print(zero_count)
print(passed_zero_count)
print(zero_count + passed_zero_count)