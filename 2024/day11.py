from functools import reduce

stones = {int(x): 1 for x in open("./2024/day11.txt").readline().strip().split()}

def split_stone(s):
    split_number = 10 ** (len(str(s)) // 2)
    left = s // split_number
    right = s % split_number
    return [left, right]

def blink(stone):
    if stone == 0:
        return [(1, 1)]
    elif len(str(stone)) % 2 == 0:
        return [(s, 1) for s in split_stone(stone)]
    else:
        return [(stone * 2024, 1)]

for i in range(75):
    blinked_stones = {}
    for s, c in stones.items():
        for b in blink(s):
            val = blinked_stones.get(b[0])
            if val:
                blinked_stones[b[0]] += (b[1] * c)
            else:
                blinked_stones[b[0]] = (b[1] * c)

    stones = blinked_stones

print(reduce(lambda sum, x: sum + x, blinked_stones.values()))