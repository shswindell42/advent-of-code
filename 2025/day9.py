from math import sqrt
from itertools import combinations
from collections import defaultdict
from functools import cache

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
areas = []
for p1, p2 in combinations(red_tiles, 2):
    area = calc_area(p1, p2)
    areas.append((p1, p2, area))
    if area > max_area:
        max_area = area
        
print(max_area)

# sort by largest area
areas.sort(key=lambda n: n[2], reverse=True)

print("generating map")
tile_map = defaultdict(lambda: defaultdict(lambda: '.'))
# num_cols = max(red_tiles, key=lambda x: x[0])[0]
# for _ in range(max(red_tiles, key=lambda x: x[1])[1] + 2):
    # row = ['.'] * num_cols
    # tile_map.append(row)

def print_map():
    for r in sorted(tile_map):
        for c in sorted(tile_map[r]):
            print(tile_map[r][c], end="")
        print()
        
def distance_direction(p1, p2):
    if p1 < p2:
        distance = p2 - p1 
        direction = -1
    else:
        distance = p1 - p2
        direction = 1
    return (distance, direction)

print("connecting red tiles")
prev_x = red_tiles[-1][0]
prev_y = red_tiles[-1][1]
for x, y in red_tiles:
    tile_map[y][x] = '#'

    distance, direction = distance_direction(prev_x, x)
    for x_offset in range(1, distance):
        tile_map[y][x + (x_offset * direction)] = 'X'
    
    distance, direction = distance_direction(prev_y, y)
    for y_offset in range(1, distance):
        tile_map[y + (y_offset * direction)][x] = 'X'
        
    prev_x = x
    prev_y = y

tile_map_groups = defaultdict(list)
for y in tile_map:
    nums = list(sorted(tile_map[y].keys()))
    groups = []
    current_group_min = nums[0]
    current_group_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_group_max = nums[i]
        else:
            groups.append((current_group_min, current_group_max))
            current_group_min = nums[i]
            current_group_max = nums[i]
    groups.append((current_group_min, current_group_max))
    
    tile_map_groups[y] = groups
    
print("filling green tiles")
#for r in tile_map:
#    # check that the row has space to fill
#    prev_c = '.'
#    edge_count = 0
#    for c in range(min(tile_map[r]), max(tile_map[r]) + 1):
#        if r in tile_map.keys():
#            if c in tile_map[r].keys() and prev_c == '.':
#                edge_count += 1
#                prev_c = tile_map[r][c]
#            elif c in tile_map[r].keys():
#                prev_c = tile_map[r][c]
#            else:
#                prev_c = '.'
    
#    if edge_count != 1:
#        inside = False
#        prev_c = '.'
#        for c in range(min(tile_map[r]), max(tile_map[r]) + 1):
#            if not inside:
#                if c in tile_map[r].keys() and prev_c == '.':
#                    inside = True
#                    prev_c = tile_map[r][c]
#            else:
#                if c not in tile_map[r].keys():
#                    tile_map[r][c] = 'X'
#                elif c in tile_map[r].keys() and prev_c == '.':
#                    inside = False
#                    prev_c = tile_map[r][c]
#                elif c in tile_map[r].keys():
#                    prev_c = tile_map[r][c]
#                else:
#                    prev_c = '.'

print("Map built")
#print_map()
@cache
def verify_point(x, y):
    valid = False
    if y in tile_map.keys():
        if x in tile_map[y].keys():
            valid = True
        else:
            edge_groups = tile_map_groups[y] 
            # how many edges groups from 0 to x?
            edge_count = 0
            if x < edge_groups[0][0]:
                valid = False
            else:
                for g in edge_groups:
                    if x < g[0]:
                        break
                    if g[0] <= x <= g[1]:
                        valid = True
                        break
                    edge_count += 1
                if edge_count % 2 == 1:
                    valid = True

    return valid
    
print(verify_point(10, 2)) # True
print(verify_point(12, 2)) # False
print(verify_point(2, 1)) # False

def verify_area(tile_map, p1, p2):
    # walk the perimeter and verify all points are red/green tiles
    distance, direction = distance_direction(p1[0], p2[0])
    for x_offset in range(distance):
        if not (verify_point(p2[0] + (x_offset * direction), p1[1])
            and verify_point(p2[0] + (x_offset * direction), p2[1])):
                return False
    distance, direction = distance_direction(p1[1], p2[1])
    for y_offset in range(distance):
        if not (verify_point(p1[0], p2[1] + (y_offset * direction))
            and verify_point(p2[0], p2[1] + (y_offset * direction))):
            return False
    return True

max_area = 0
count = 0
for space in areas:
    p1, p2, area = space
    if verify_area(tile_map, p1, p2):
        max_area = area
        break
    count += 1
    if count % 1000 == 0:
        print(count)

print(max_area)
