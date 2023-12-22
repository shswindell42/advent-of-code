
def print_geography(geography: list[list[str]]) -> None:
    for l in geography:
        for c in l:
            print(c, end="")
        print()
    print()

directions = {
    "north": (-1, 0)
    ,"west": (0, -1)
    ,"south": (1, 0)
    ,"east": (0, 1)
}


def spin_cycle(geography: list[list[str]]) -> None:
    for direction in directions.keys():

        if direction == "north":
            column_start = 0
            column_end = len(geography[0]) - 1
            row_start = 0
            row_end = len(geography) - 1
        elif direction == "south":
            column_start = 0
            column_end = len(geography[0]) - 1
            row_start = len(geography) - 1
            row_end = 0
        elif direction == "east":
            column_start = len(geography[0]) - 1
            column_end = 0
            row_start = 0
            row_end = len(geography) - 1
        elif direction == "west":
            column_start = 0
            column_end = len(geography[0]) - 1
            row_start = 0
            row_end = len(geography) - 1

        column_index = column_start

        # for each column
        while column_index >= 0 and column_index < len(geography[0]):
            # examine each row in the column
            # when a 'O' is found, move it up until a '#' is reached
            row_index = row_start
            while row_index >= 0 and row_index < len(geography):
                if geography[row_index][column_index] == 'O':
                    #move the rock
                    if direction == "north":
                        range_end = row_index + 1
                    elif direction == "south":
                        range_end = len(geography) - row_index + 1
                    elif direction == "east":
                        range_end = len(geography[0]) - column_index + 1
                    elif direction == "west":
                        range_end = column_index + 1

                    for offset in range(1, range_end):
                        row_offset = row_index + (offset * directions[direction][0])
                        column_offset = column_index + (offset * directions[direction][1])

                        if row_offset >= 0 and row_offset < len(geography) and column_offset >= 0 and column_offset < len(geography[0]):
                            space = geography[row_offset][column_offset]
                            if space == '.':
                                geography[row_offset - directions[direction][0]][column_offset - directions[direction][1]] = '.'
                                geography[row_offset][column_offset] = 'O'
                                #print_geography(geography)
                            elif space in "#O":
                                break
                
                row_index -= (1 if row_start > 0 else -1)
            
            column_index -= (1 if column_start > 0 else -1)


def calc_score(geography: list[list[str]]) -> int:
    score = 0
    for i, r in enumerate(reversed(geography)):
        big_rocks = len([b for b in r if b == 'O'])
        score += big_rocks * (i+1)
    
    return score

def solve(geography: list[list[str]]) -> int:
    
    # keep track of the last few scores, if they stay the same then stop the cycle
    scores = []
    cycle_count = 1000000000
    for cycle in range(cycle_count):
        spin_cycle(geography)
        scores.append(calc_score(geography))

        # max cycle is set to 100 (arbitrary)
        for cycle_size in range(3, 100):
            for n in range(len(scores) - cycle_size):
                if scores[n:n+cycle_size] == scores[n+cycle_size:n+(cycle_size * 2)]:
                    cycle_offset = ((cycle_count - n) % (cycle - n)) + n
                    return scores[cycle_offset]

    # todo: replace with index based on the 1000000000 iteration
    return scores[-1]

geography = []
with open("./day14sample.txt", "r") as fp:
    for line in fp.readlines():
        geography.append([*line.strip()])

print_geography(geography)
load = solve(geography)
print_geography(geography)
print(load)