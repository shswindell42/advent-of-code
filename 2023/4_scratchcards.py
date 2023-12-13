pointTotal = 0
points = 0

with open('./day4.txt', 'r') as fp:
    lines = fp.readlines()

copys = [1] * len(lines)
for idx, line in enumerate(lines):
    for c in range(copys[idx]):
        numbers = line.split(':')[1]
        winning, scratch = numbers.split("|")
        winningNumbers = [int(w.strip()) for w in winning.strip().split(" ") if w]
        scratchNumbers = [int(s.strip()) for s in scratch.strip().split(" ") if s]

        point = 0
        for s in scratchNumbers:
            if s in winningNumbers:
                point = point * 2 if point else 1
        
        pointTotal += point

        # increment copys
        offset = 1
        while point > 0:
            copys[idx + offset] += 1
            point = point // 2
            offset += 1

print(pointTotal)
print(sum(copys))