from math import sqrt
from itertools import combinations

junctions = []
with open("./2025/day8.txt", "r") as fp:
    for line in fp.readlines():
        line = line.strip()
        x, y, z = line.split(",")
        junctions.append((int(x), int(y), int(z)))

# calculate the distance for each pair
def distance(p1, p2):
    x = (p1[0] - p2[0]) ** 2
    y = (p1[1] - p2[1]) ** 2
    z = (p1[2] - p2[2]) ** 2
    
    return sqrt(x + y + z)

junction_pairs = [
                    (c[0], c[1], distance(junctions[c[0]], junctions[c[1]]))
                    for c in combinations(range(len(junctions)), 2)
                ]
# junction_pairs = []
# for i, p in enumerate(junctions):
#     for j, q in enumerate(junctions[i+1:]):
#         if i != j:
#             d = distance(p, q)
#             junction_pairs.append((i, j, d))

# sort based on distance, closest pairs first
junction_pairs.sort(key=lambda p: p[2])

def find_in_sets(sets, value):
    for i, s in enumerate(sets):
        if value in s:
            return i

# group the junctions based on distance
junction_sets = [{j} for j in range(len(junctions))]

connections_made = 0
for i in range(1000):
    p, q, _ = junction_pairs[i]
    p_set_index = find_in_sets(junction_sets, p) 
    q_set_index = find_in_sets(junction_sets, q)
    if p_set_index != q_set_index:
        junction_sets[p_set_index] = junction_sets[p_set_index] | junction_sets[q_set_index]
        del junction_sets[q_set_index]

junction_sets.sort(key=lambda s: len(s), reverse=True)

total = 1
for i in range(3):
    total *= len(junction_sets[i])

print(total)