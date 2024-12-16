
directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}

def move_robot(map, robot_position, instruction, test=False):
    direction = directions[instruction]
    next_position = (robot_position[0] + direction[0], robot_position[1] + direction[1])
    neighbor = map[next_position[1]][next_position[0]]
    
    if neighbor == ".":
        if not test:
            map[next_position[1]][next_position[0]] = map[robot_position[1]][robot_position[0]]
            map[robot_position[1]][robot_position[0]] = '.'
        robot_position = next_position
    elif neighbor in ('[',']') and instruction in ('<', '>'):
        moved_position = move_robot(map, next_position, instruction)   
        if moved_position != next_position: 
            map[next_position[1]][next_position[0]] = map[robot_position[1]][robot_position[0]]
            map[robot_position[1]][robot_position[0]] = '.'
            robot_position = next_position
    elif neighbor == '[' and instruction in ('^', 'v'):
        right_position = (next_position[0] + 1, next_position[1])
        moved_position_left = move_robot(map, next_position, instruction, True)
        moved_position_right = move_robot(map, right_position, instruction, True)
        
        if moved_position_left != next_position and moved_position_right != right_position and moved_position_left[1] == moved_position_right[1]:
            if not test:
                move_robot(map, next_position, instruction)
                move_robot(map, right_position, instruction)
                map[next_position[1]][next_position[0]] = map[robot_position[1]][robot_position[0]]
                map[right_position[1]][right_position[0]] = '.'
                map[robot_position[1]][robot_position[0]] = '.'
            robot_position = next_position
    elif neighbor == ']' and instruction in ('^', 'v'):
        left_position = (next_position[0] - 1, next_position[1])
        moved_position_left = move_robot(map, left_position, instruction, True)
        moved_position_right = move_robot(map, next_position, instruction, True)
        
        if moved_position_right != next_position and moved_position_left != left_position and moved_position_right[1] == moved_position_left[1]:
            if not test:
                move_robot(map, left_position, instruction)
                move_robot(map, next_position, instruction)
                map[next_position[1]][next_position[0]] = map[robot_position[1]][robot_position[0]]
                map[left_position[1]][left_position[0]] = '.'
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
            row = []
            for c in l:
                if c == '#':
                    row.extend(['#', '#'])
                elif c == 'O':
                    row.extend(['[', ']'])
                elif c == '.':
                    row.extend(['.', '.'])
                elif c == '@':
                    row.extend(['@', '.'])
                    y = len(map)
                    x = len(row) - 2
                    robot_position = (x, y)
            map.append(row)
        else:
            for instruction in l:
                robot_position = move_robot(map, robot_position, instruction)
                # print(f"Move {instruction}")
                # print_map(map)
        
total = 0
for y, r in enumerate(map):
    for x, c in enumerate(r):
        if c == '[':
            total += 100 * y + x

print(total)