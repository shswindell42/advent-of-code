from math import sqrt
from itertools import combinations

def calc_area(p1, p2):
    a = sqrt((p1[0] - p2[0]) ** 2) + 1
    b = sqrt((p1[1] - p2[1]) ** 2) + 1
    return int(a * b)

red_tiles = []
with open("./2025/day9.txt", "r") as fp:
    for line in fp.readlines():
        x, y = line.strip().split(",")
        red_tiles.append((int(x), int(y)))
        
max_area = 0
for p1, p2 in combinations(red_tiles, 2):
    area = calc_area(p1, p2)
    if area > max_area:
        max_area = area
        
print(max_area)