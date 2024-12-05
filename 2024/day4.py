def bounds_check(map, x, y):
    x_max = len(map[0])
    y_max = len(map)
    return 0 <= x < x_max and 0 <= y < y_max

def search_horizontal(map, x, y):
    return map[y][x:x+4] in ['XMAS', 'SAMX']

def search_vertical(map, x, y):
    return "".join([s[x] for s in map[y:y+4]]) in ['XMAS', 'SAMX']

def search_diagonal(map, x, y):
    diagonal_count = sum(
        [
            "".join([s[x+i] for i, s in enumerate(map[y:y+4]) if bounds_check(map, x + i, y)]) == 'XMAS'
            ,"".join([s[x+i] for i, s in enumerate(reversed(map[y-3:y+1])) if bounds_check(map, x + i, y)]) == 'XMAS'
            ,"".join([s[x-i] for i, s in enumerate(map[y:y+4]) if bounds_check(map, x - i, y)]) == 'XMAS'
            ,"".join([s[x-i] for i, s in enumerate(reversed(map[y-3:y+1])) if bounds_check(map, x - i, y)]) == 'XMAS'
        ]
    )
    return diagonal_count

def search_x_mas(map, x, y):
    top_left = map[y+1][x-1] if bounds_check(map, x-1, y+1) else ''
    top_right = map[y+1][x+1] if bounds_check(map, x+1, y+1) else ''
    bottom_left = map[y-1][x-1] if bounds_check(map, x-1, y-1) else ''
    bottom_right = map[y-1][x+1] if bounds_check(map, x+1, y-1) else ''
    middle = map[y][x] # always "A"
    
    a = top_left + middle + bottom_right
    b = top_right + middle + bottom_left
    return a in ['MAS', 'SAM'] and b in ['MAS', 'SAM']

xmas_count = 0
x_mas_count = 0
map = []
with open("./2024/day4.txt", "r") as fp:
    for line in fp.readlines():
        map.append(line.strip())
        
for y, r in enumerate(map):
    for x in range(len(r)):
        if search_horizontal(map, x, y):
            xmas_count += 1
            print(f"horizontal: ({x}, {y})")
        
        if search_vertical(map, x, y):
            xmas_count += 1
            print(f"vertical: ({x}, {y})")
        
        diagonal_count = search_diagonal(map, x, y)
        if diagonal_count > 0:
            xmas_count += diagonal_count
            print(f"diagonal: ({x}, {y}) x {diagonal_count}")
            
        if map[y][x] == 'A' and search_x_mas(map, x, y):
            x_mas_count += 1
            print(f"X-MAS at ({x}, {y})")
            
print(xmas_count)
print(x_mas_count)
