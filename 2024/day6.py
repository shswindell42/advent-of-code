map = []
with open("./2024/day6.txt") as fp:
    row = 0
    for line in fp.readlines():
        map.append(list(line.strip()))
        if '^' in line:
            position = (line.find('^'), row, "up")
        row += 1

# Floyd's tortoise and hare algorithm for cycle detection
def in_cycle(f):
    try:
        ti = 0
        t = f[ti]
        hi = 1
        h = f[hi]
        while t != h:
            ti += 1
            hi += 2
            t = f[ti]
            h = f[hi]
            
        return True 
    except:
        return False

def navigate_guard(map, position, steps = []):
    directions = {
        "up": (0, -1),
        "right": (1, 0),
        "down": (0, 1),
        "left": (-1, 0)
    }

    rotation_order = ["up", "right", "down", "left"]
    spin = 0
    while True:
        direction = directions[rotation_order[spin]]
        next_step = (position[0] + direction[0], position[1] + direction[1], rotation_order[spin])
        
        if 0 <= next_step[0] < len(map[0]) and 0 <= next_step[1] < len(map):
            next_step_value = map[next_step[1]][next_step[0]]
            if next_step_value == '#':
                spin = (spin + 1) % 4
            else:
                steps.append(position)
                position = next_step
                if len(steps) % 1000 == 0:
                    if in_cycle(steps):
                        return steps, True
        else:
            steps.append(position)
            break
        
    return steps, False

footsteps, _ = navigate_guard(map, position, [])
footstep_locations = set([(f[0], f[1]) for f in footsteps])
print(len(footstep_locations))

cycle_count = 0
for s in list(footstep_locations):
    map[s[1]][s[0]] = "#"
    new_footsteps, is_cycle = navigate_guard(map, position, [])
    if is_cycle:
        cycle_count += 1
    map[s[1]][s[0]] = "."

print(cycle_count)