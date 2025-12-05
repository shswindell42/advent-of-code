
neighbor_offsets = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
    "top_left": (-1, -1),
    "top_right": (1, -1),
    "bottom_right": (1, 1),
    "bottom_left": (-1, 1)
}

with open("./2025/day4.txt", "r") as fp:
    map = [l.strip() for l in fp.readlines()]
    total_rows = len(map)
    total_cols = len(map[0])

total_rolls_removed = 0
accessable_paper_rolls = -1    
while accessable_paper_rolls != 0:
    accessable_paper_rolls = 0    

    for y, row in enumerate(map):
        for x, value in enumerate(row):
            if value == "@":
                paper_count = 0
                for offset in neighbor_offsets.values():
                    neighbor_x = x + offset[0]
                    neighbor_y = y + offset[1]
                
                    # bounds check
                    if (0 <= neighbor_x < total_cols 
                        and 0 <= neighbor_y < total_rows):
                        if map[neighbor_y][neighbor_x] == "@":
                            paper_count += 1
                        
                            if paper_count >= 4:
                                break
            
                if paper_count < 4:
                    accessable_paper_rolls += 1
                    # update the map 
                    map[y] = map[y][:x] + "x" + map[y][x+1:]

    total_rolls_removed += accessable_paper_rolls
                
print(total_rolls_removed)