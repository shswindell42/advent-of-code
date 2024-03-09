directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

def add_visited_space(visited_spaces: list[tuple[int,int]], space: tuple[int,int]) -> None:
    if space not in visited_spaces:
        visited_spaces.append(space)

# runs a light beam (laser) through the layout from the starting point in the given direction
# returns a distinct list of visited locations
def shoot_laser(layout: list[str], start: tuple[int,int], direction: str, visited_spaces: list[tuple[int,int]] = [], past_starting_directions: list[tuple[int,int,str]] = []) -> list[tuple[int, int]]:
    if (*start, direction) in past_starting_directions:
        return visited_spaces
    else:
        past_starting_directions.append((*start, direction))
    
    current_location = start
    while True:

        next_location = (current_location[0] + directions[direction][0], current_location[1] + directions[direction][1])

        if next_location[0] >= 0 and next_location[0] < len(layout) and next_location[1] >= 0 and next_location[1] < len(layout[0]):
            add_visited_space(visited_spaces, next_location)
            next_space = layout[next_location[0]][next_location[1]]
            if next_space == '.':
                current_location = next_location
            elif next_space == '/':
                if direction == 'up':
                    shoot_laser(layout, next_location, 'right', visited_spaces, past_starting_directions)
                elif direction == 'down':
                    shoot_laser(layout, next_location, 'left', visited_spaces, past_starting_directions)
                elif direction == 'right':
                    shoot_laser(layout, next_location, 'up', visited_spaces, past_starting_directions)
                elif direction == 'left':
                    shoot_laser(layout, next_location, 'down', visited_spaces, past_starting_directions)
                break
            elif next_space == '\\':
                if direction == 'up':
                    shoot_laser(layout, next_location, 'left', visited_spaces, past_starting_directions)
                elif direction == 'down':
                    shoot_laser(layout, next_location, 'right', visited_spaces, past_starting_directions)
                elif direction == 'right':
                    shoot_laser(layout, next_location, 'down', visited_spaces, past_starting_directions)
                elif direction == 'left':
                    shoot_laser(layout, next_location, 'up', visited_spaces, past_starting_directions)
                break
            elif next_space == '|':
                if direction == 'right' or direction == 'left':
                    shoot_laser(layout, next_location, 'down', visited_spaces, past_starting_directions)
                    shoot_laser(layout, next_location, 'up', visited_spaces, past_starting_directions)
                    break
                else:
                    current_location = next_location
            elif next_space == "-":
                if direction == 'up' or direction == 'down':
                    shoot_laser(layout, next_location, 'left', visited_spaces, past_starting_directions)
                    shoot_laser(layout, next_location, 'right', visited_spaces, past_starting_directions)
                    break
                else:
                    current_location = next_location
        else:
            break

    return visited_spaces



layout: list[str]
with open('./day16.txt', 'r') as fp:
    layout = [line.strip() for line in fp.readlines()]

visited_spaces = shoot_laser(layout, (0, -1), 'right')

#print(visited_spaces)
print(f"Starting from the top-left going right energizes {len(visited_spaces)} tiles")

max_energized_tiles = 0
for row_index in range(len(layout)):
    energized_tiles_left = shoot_laser(layout, (row_index, -1), 'right', [], [])
    energized_tiles_right = shoot_laser(layout, (row_index, len(layout[row_index])), 'left', [], [])
    max_energized_tiles = max(max_energized_tiles, len(energized_tiles_right), len(energized_tiles_left))

for column_index in range(len(layout[0])):
    energized_tiles_top = shoot_laser(layout, (-1, column_index), 'down', [], [])
    energized_tiles_bottom = shoot_laser(layout, (len(layout), column_index), 'up', [], [])
    max_energized_tiles = max(max_energized_tiles, len(energized_tiles_top), len(energized_tiles_bottom))

print(f"Up to {max_energized_tiles} can be energized")