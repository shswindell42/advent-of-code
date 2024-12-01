from dataclasses import dataclass

@dataclass
class DigCommand:
    direction: str
    length: int
    color: str
    
    
def print_map(map, filename):
    with open(filename, "w") as fp:
        for r in map:
            fp.write(r + '\n')

# read the file and build the command list
commands: list[DigCommand] = []
with open('day18.txt', 'r') as fp:
    for line in fp.readlines():
        l = line.strip().split(' ')
        commands.append(DigCommand(l[0], int(l[1]), l[2]))
        
map: list[str] = ['#']
current_location: tuple[int,int] = (0,0)
for command in commands:
    if command.direction == 'R':
        # append as needed
        length = len(map[0])
        if current_location[1] + command.length >= length:
            additional_space = current_location[1] + command.length - length + 1
            for i, r in enumerate(map):
                map[i] = map[i] + ('.' * additional_space)
        
        
        l = map[current_location[0]]
        map[current_location[0]] = l[0:current_location[1] + 1] + '#' * command.length + l[current_location[1] + command.length + 1:]
        
        current_location = (current_location[0], current_location[1] + command.length)    
    
    elif command.direction == 'L':
        # prepend as needed
        if current_location[1] - command.length < 0:
            additional_space = command.length - current_location[1]
            for i, r in enumerate(map):
                map[i] = ('.' * additional_space) + map[i] 
            current_location = (current_location[0], current_location[1] + additional_space)
        
        
        l = map[current_location[0]]
        map[current_location[0]] = l[0:current_location[1] - command.length] + '#' * command.length + l[current_location[1]:]
        
        current_location = (current_location[0], current_location[1] - command.length)  
        
    elif command.direction == 'U':
        # add rows to the beginning as needed
        if current_location[0] - command.length < 0:
            additional_space = command.length - current_location[0]
            line_length = len(map[0])
            map = ['.' * line_length] * additional_space + map
            current_location = (current_location[0] + additional_space, current_location[1])
            
        for i in range(current_location[0] - command.length, current_location[0] + 1):
            map[i] = map[i][:current_location[1]] + '#' + map[i][current_location[1] + 1:]
            
        current_location = (current_location[0] - command.length, current_location[1])
    
    elif command.direction == 'D':
        length = len(map)
        if current_location[0] + command.length >= length:
            additional_space = command.length + current_location[0] - length + 1
            line_length = len(map[0])
            map = map + ['.' * line_length] * additional_space
            
        for i in range(current_location[0], current_location[0] + command.length + 1):
            map[i] = map[i][:current_location[1]] + '#' + map[i][current_location[1] + 1:]
            
        current_location = (current_location[0] + command.length, current_location[1])
        
    # print("-" * 20)
    # print(command)
    # for r in map:
    #     print(r)
    # print("-" * 20)
    # print(f"{command} -> {current_location} mapsize=({len(map)}, {len(map[0])})")
    
print_map(map, "map.txt")

for i, r in enumerate(map):
    on_edge = False
    inside = False
    for j, c in enumerate(r):
        if on_edge:
            if c == '.':
                on_edge = not on_edge
                inside = not inside
        else:
            if c == '#':
                on_edge = not on_edge
        
        if inside:
            if c == '.':
                map[i] = map[i][:j] + '#' + map[i][j+1:]
            if c == '#':
                inside = False
                

print_map(map, "map_filled.txt")

fill = 0
for i, r in enumerate(map):
    for j, c in enumerate(r):
        if c == "#":
            fill += 1
            
        #examine the rest of the line to find groups of # and .
        # if # is odd then outside else inside
        
        
print(f"fill={fill}")

# for r in map:
#     print(r)