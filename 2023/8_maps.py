import math

map = {}
with open('./day8.txt', 'r') as fp:
    instructions = fp.readline().strip()
    fp.readline() # blank line
    for line in fp.readlines():
        data = line.split("=")
        node = data[0].strip()
        connections = data[1].strip().replace("(", "").replace(")", "").split(', ')
        map[node] = (connections[0], connections[1])

curNodes = [x for x in map.keys() if x[-1] == 'A']

steps_to_z = []
for c in curNodes:
    curNode = c
    steps = 0
    while curNode[-1] != 'Z':
        direction = instructions[((steps + 1) % len(instructions)) - 1]
        curNode = map[curNode][0] if direction == "L" else map[curNode][1]
        steps += 1
    steps_to_z.append(steps)

print(steps_to_z)
print(math.lcm(*steps_to_z))