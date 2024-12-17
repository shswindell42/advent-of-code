import heapq

directions = [
    (1, 0) # east
    ,(0, -1) # north
    ,(-1, 0) # west
    ,(0, 1) # south
]

map = []
with open("./2024/day16sample.txt") as fp:
    for line in fp:
        map.append(line.strip())

# start position is always at the same place
current_position = (1, len(map) - 2)
current_direction_index = 0
cost = 0

# end position is always at the same place
end_position = (len(map[1]) - 2, 1)

visited = [] # list of points already visited on the map
queue = []
heapq.heappush(queue, (0, current_position, current_direction_index))

while len(queue) > 0:
    cost, current_position, current_direction_index = heapq.heappop(queue)
    
    if (current_position, current_direction_index) in visited:
        continue
    
    visited.append((current_position, current_direction_index))

    #check for end here
    if current_position == end_position:
        break
    
    # push the next step into the queue if possible
    direction = directions[current_direction_index]
    forward_position = (current_position[0] + direction[0], current_position[1] + direction[1])
    if map[forward_position[1]][forward_position[0]] in '.SE':
        heapq.heappush(queue, (cost + 1, forward_position, current_direction_index))
        
    # rotate clockwise
    clockwise_direction_index = (current_direction_index - 1) % 4
    clockwise_direction = directions[clockwise_direction_index]
    clockwise_step = (current_position[0] + clockwise_direction[0], current_position[1] + clockwise_direction[1])
    if map[clockwise_step[1]][clockwise_step[0]] in '.SE':
        heapq.heappush(queue, (cost + 1001, clockwise_step, clockwise_direction_index))
    
    # rotate counter-clockwise
    counter_clockwise_direction_index = (current_direction_index + 1) % 4
    counter_clockwise_direction = directions[counter_clockwise_direction_index]
    counter_clockwise_step = (current_position[0] + counter_clockwise_direction[0], current_position[1] + counter_clockwise_direction[1])
    if map[counter_clockwise_step[1]][counter_clockwise_step[0]] in '.SE':
        heapq.heappush(queue, (cost + 1001, counter_clockwise_step, counter_clockwise_direction_index))

visited_seats = [x[0] for x in visited]
for y, r in enumerate(map):
    for x, c in enumerate(r):
        if (x,y) in visited_seats:
            print("O", end="")
        else:
            print(c, end="")
    print("")
    
print(cost)