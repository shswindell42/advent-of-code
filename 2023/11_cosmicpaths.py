universe: list[list[str]] = []
with open('./day11.txt', 'r') as fp:
    for line in fp.readlines():
        universe.append([*line.strip()])


# find empty rows and columns
emptyRows: list[int] = []
for i, r in enumerate(universe):
    if set(r) == {'.'}:
        emptyRows.append(i)

emptyCols: list[int] = []
for i in range(0, len(universe[0])):
    if set([x[i] for x in universe]) == {'.'}:
        emptyCols.append(i)

# # expand the universe
expansion_size = 999999
# print("Expanding Columns of the universe")
# for i, c in enumerate(emptyCols):
#     for r in universe:
#         for e in range(expansion_size):
#             r.insert(c + (i * expansion_size) + e, '.')
    
# print("Expanding Rows of the universe")
# for i, r in enumerate(emptyRows):
#     row = universe[r + (i * expansion_size)]
#     for e in range(expansion_size):
#         universe.insert(r + (i * expansion_size) + e, row)


# for r in universe:
#     for c in r:
#         print(c, end="")
#     print()

# find all galaxies
galaxys: list[tuple[int, int]] = []
for i, r in enumerate(universe):
    for j, c in enumerate(r):
        if c == '#':
            galaxys.append((i, j))


# pair up each galaxy
galaxys_pairs = [(a, b) for idx, a in enumerate(galaxys) for b in galaxys[idx + 1:]]
sum_distance = 0
for a, b in galaxys_pairs:
    sum_distance += abs(a[0] - b[0]) + abs(a[1] - b[1])
    if a[0] > b[0]:
        sum_distance += len([x for x in emptyRows if x <= a[0] and x >= b[0]]) * expansion_size
    else:
        sum_distance += len([x for x in emptyRows if x >= a[0] and x <= b[0]]) * expansion_size
    
    if a[1] > b[1]:
        sum_distance += len([x for x in emptyCols if x <= a[1] and x >= b[1]]) * expansion_size
    else:
        sum_distance += len([x for x in emptyCols if x >= a[1] and x <= b[1]]) * expansion_size
    
    
print(f"The sum of the shortest distances is {sum_distance}")