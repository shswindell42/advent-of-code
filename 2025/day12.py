shapes = []
spaces = []

with open("./2025/day12.txt", "r") as fp:
    reading = True
    while reading:
        line = fp.readline().strip()
        if not line:
            break
        split_line = line.split(":")
        if not split_line[1]:
            index = line.split(":")[0]
            shape = []
            for i in range(3):
                shape_line = fp.readline().strip()
                shape.append(shape_line)
            
            shapes.append(shape)
            fp.readline()
        elif split_line[1]:
            dim, reqs = line.split(":")
            x, y = dim.split("x")
            space = ((int(x), int(y),), [int(s) for s in reqs.strip().split(" ")])
            spaces.append(space)


present_used_spaces = []
for shape in shapes:
    used_space = 0
    for s in shape:
        used_space += sum([1 for i in s if i == '#'])
    present_used_spaces.append(used_space)

presents_fit_count = 0
for space in spaces:
    area = space[0][0] * space[0][1]
    required_space = sum(space[1]) * 9
    
    required_used_space = sum([present_used_spaces[i] * space[1][i] for i in range(len(space[1]))])
    
    if required_space <= area:
        presents_fit_count += 1

print(presents_fit_count)