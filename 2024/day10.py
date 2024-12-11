directions = [
    (0, -1), # up
    (0, 1),  # down
    (-1, 0), # left
    (1, 0)   # right
]

starting_points = []
map = []
with open("./2024/day10.txt") as fp:
    for y, line in enumerate(fp.readlines()):
        line_numbers = []
        for x, p in enumerate(line.strip()):
            if p == '0':
                starting_points.append((x, y))
            line_numbers.append(int(p))
        map.append(line_numbers)
                
def find_trails(map, start, unique):
    if map[start[1]][start[0]] == 9:
        return [start]
    
    end_points = []
    for direction in directions:
        next_step = (start[0] + direction[0], start[1] + direction[1])
        if 0 <= next_step[0] < len(map[0]) and 0 <= next_step[1] < len(map):
            if map[next_step[1]][next_step[0]] == map[start[1]][start[0]] + 1:
                ends = find_trails(map, next_step, unique)
                for e in ends:
                    if e not in end_points or not unique:
                        end_points.append(e)
            
    return end_points

total_score = 0
for p in starting_points:
    total_score += len(find_trails(map, p, False))

print(total_score)