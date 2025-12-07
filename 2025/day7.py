from functools import cache

with open("./2025/day7.txt", "r") as fp:
    lines = [list(l.strip()) for l in fp.readlines()]

splitter_hits = []
prev_line = lines[0]
for r, line in enumerate(lines[1:]):
    for i, pair in enumerate(zip(prev_line, line)):
        p, c = pair
        if p == "S":
            lines[r+1][i] = '|'
        elif p == "|" and c != '^':
            lines[r+1][i] = '|'
        elif p == "|" and c == '^':
            lines[r+1][i-1] = '|'
            lines[r+1][i+1] = '|'
            splitter_hits.append((i, r+1))
    prev_line = line

# for r in lines:
    # for c in r:
        # print(c, end="")
    # print()
print(len(set(splitter_hits)))


# part 2 done recursively
# use memoization (@cache) to store results based on input
# this reduces recalculating the same answer multiple times

with open("./2025/day7.txt", "r") as fp:
    manifold = [l.strip() for l in fp.readlines()]

# find the start spot
start = (manifold[0].find("S"), 0)

@cache
def traverse_particle(start):
    if start[1] == len(manifold) - 1:
        return 1
    
    # look below the start position
    next = manifold[start[1] + 1][start[0]]
    if next == "^":
        left = (start[0] - 1, start[1] + 1)
        right = (start[0] + 1, start[1] + 1)
        return traverse_particle(left) + traverse_particle(right)
    
    down = (start[0], start[1] + 1)
    return traverse_particle(down)

total_timelines = traverse_particle(start)
print(total_timelines)