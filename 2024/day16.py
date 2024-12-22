import heapq
import sys

directions = [
    (1, 0) # east
    ,(0, -1) # north
    ,(-1, 0) # west
    ,(0, 1) # south
]

map = []
with open("./2024/day16.txt") as fp:
    for line in fp:
        map.append([c for c in line.strip()])

def backtrack(map, pos):
    prev_paths = paths.get(pos, [])
    for p,d in prev_paths:
        if p:
            map[p[1]][p[0]] = 'O' 
            backtrack(map, (p, d))
            

# start position is always at the same place
current_position = (1, len(map) - 2)
current_direction_index = 0
cost = 0

# end position is always at the same place
end_position = (len(map[1]) - 2, 1)

visited = {}
queue = []
paths = {}
lowest_cost_points = []
lowest_cost = sys.maxsize
heapq.heappush(queue, (0, current_position, current_direction_index, None, None))

while len(queue) > 0:
    cost, current_position, current_direction_index, prev_position, prev_direction_index = heapq.heappop(queue)
    
    visited_cost = visited.get((current_position, current_direction_index))
    if visited_cost and visited_cost < cost:
        continue
            
    visited[(current_position, current_direction_index)] = cost
    
    prev_paths = paths.get((current_position, current_direction_index))
    if not prev_paths:
        paths[(current_position, current_direction_index)] = [(prev_position, prev_direction_index)]
    else:
        if not (prev_position, prev_direction_index) in prev_paths:
            paths[(current_position, current_direction_index)].append((prev_position, prev_direction_index))

    #check for end here
    if current_position == end_position:
        if cost <= lowest_cost:
            lowest_cost = cost
            lowest_cost_points.append((current_position, current_direction_index))
            print("Shortest path found")
            continue
        else:
            break
    
    # push the next step into the queue if possible
    direction = directions[current_direction_index]
    forward_position = (current_position[0] + direction[0], current_position[1] + direction[1])
    if map[forward_position[1]][forward_position[0]] in '.SE':
        heapq.heappush(queue, (cost + 1, forward_position, current_direction_index, current_position, current_direction_index))
        
    # rotate clockwise
    clockwise_direction_index = (current_direction_index - 1) % 4
    #heapq.heappush(queue, (cost + 1000, current_position, clockwise_direction_index, prev_position, current_direction_index))
    clockwise_direction = directions[clockwise_direction_index]
    clockwise_step = (current_position[0] + clockwise_direction[0], current_position[1] + clockwise_direction[1])
    if map[clockwise_step[1]][clockwise_step[0]] in '.SE':
        heapq.heappush(queue, (cost + 1001, clockwise_step, clockwise_direction_index, current_position, current_direction_index))
    
    # rotate counter-clockwise
    counter_clockwise_direction_index = (current_direction_index + 1) % 4
    # heapq.heappush(queue, (cost + 1000, current_position, counter_clockwise_direction_index, prev_position, current_direction_index))
    counter_clockwise_direction = directions[counter_clockwise_direction_index]
    counter_clockwise_step = (current_position[0] + counter_clockwise_direction[0], current_position[1] + counter_clockwise_direction[1])
    if map[counter_clockwise_step[1]][counter_clockwise_step[0]] in '.SE':
        heapq.heappush(queue, (cost + 1001, counter_clockwise_step, counter_clockwise_direction_index, current_position, current_direction_index))


map[end_position[1]][end_position[0]] = 'O'
for p, d in lowest_cost_points:
    backtrack(map, (p, d))

seat_count = 0
for y, r in enumerate(map):
    for x, c in enumerate(r):
        print(c, end="")
        if c == 'O':
            seat_count += 1
    print("")
    
print(lowest_cost)
print(seat_count)