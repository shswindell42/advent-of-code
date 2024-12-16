
directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}

def move_robot(map, robot_position, instruction):
    direction = directions[instruction]
    next_position = (robot_position[0] + direction[0], robot_position[1] + direction[1])
    neighbor = map[next_position[1]][next_position[0]]
    
    if neighbor == ".":
        map[next_position[1]][next_position[0]] = map[robot_position[1]][robot_position[0]]
        map[robot_position[1]][robot_position[0]] = '.'
        robot_position = next_position
    elif neighbor == "O":
        moved_position = move_robot(map, next_position, instruction)   
        if moved_position != next_position: 
            map[next_position[1]][next_position[0]] = map[robot_position[1]][robot_position[0]]
            map[robot_position[1]][robot_position[0]] = '.'
            robot_position = next_position

    return robot_position

def print_map(map):
    for r in map:
        for c in r:
            print(c, end="")
        print("")

map = []
robot_position = (0,0)

with open("./2024/day15.txt") as f:
    reading_map = True
    for line in f:
        l = line.strip()
        if l == "":
            reading_map = False
            continue
        
        if reading_map:
            map.append([c for c in l])
            if '@' in l:
                y = len(map) - 1
                x = l.index('@')
                robot_position = (x, y)
        else:
            for instruction in l:
                robot_position = move_robot(map, robot_position, instruction)
                #print(f"Move {instruction}")
                #print_map(map)
        
total = 0
for y, r in enumerate(map):
    for x, c in enumerate(r):
        if c == 'O':
            total += 100 * y + x
        
print(total)