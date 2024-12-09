antenna = {}
map = []
with open("./2024/day8.txt") as fp:
    for y, line in enumerate(fp.readlines()):
        map.append(line.strip())
        for x, c in enumerate(line.strip()):
            if c != '.':
                if antenna.get(c):
                    antenna.get(c).append((x, y))
                else:
                    antenna[c] = [(x, y)]

antinodes = []
for a in antenna.keys():
    for n in antenna[a]:
        for m in antenna[a]:
            if n != m:
                # calc the antinode of this pair
                x_diff = m[0] - n[0]
                y_diff = m[1] - n[1]
                
                r = n
                
                while True:
                    antinode = (r[0] - x_diff, r[1] - y_diff)
                    r = antinode
                    if 0 <= antinode[0] < len(map[0]) and 0 <= antinode[1] < len(map):
                        if antinode not in antinodes:
                            antinodes.append(antinode)
                    else:
                        break
                    
    # determine if the nodes have antinodes
    if len(antenna[a]) >= 3:
        for n in antenna[a]:
            if n not in antinodes:
                antinodes.append(n)
                     
print(len(antinodes))