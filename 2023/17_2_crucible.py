import sys
from queue import PriorityQueue

def inbounds(space: list[list[int]], location: tuple[int, int]) -> bool:
    return location[0] >= 0 and location[0] < len(space) and location[1] >= 0 and location[1] < len(space[0])

def add_location_to_queue(queue: PriorityQueue, location: tuple[int, int], step: tuple[int, int], weight: int, direction: str, direction_count: int) -> None:
    distance = distances[location] + weight
    if distance < distances[step]:
        distances[step] = distance
        if (*step, direction) not in visited_nodes:
            visited_nodes.append((*step, direction))
            queue.put((distance, step, direction, direction_count))


with open('./day17sample.txt', 'r') as fp:
    pattern: list[list[int]] = []
    for l in fp.readlines():
        pattern.append(list([int(c) for c in l.strip()]))
        

distances = {}
for i, r in enumerate(pattern):
    for j, c in enumerate(r):
        distances[(i, j)] = sys.maxsize
distances[(0,0)] = 0        
        
visited_nodes: list[tuple[int, int, str]] = []
priority = PriorityQueue()

priority.put((0, (0,0), "start", 1))

target = (len(pattern) - 1, len(pattern[0]) - 1)
straight_line_distance_max = 3

while not priority.empty():
    weight, current_location, direction, direction_count = priority.get()
    
    # if current_location == target:
    #     break
    
    right_location = (current_location[0], current_location[1] + 1)
    left_location = (current_location[0], current_location[1] - 1)
    up_location = (current_location[0] - 1, current_location[1])
    down_location = (current_location[0] + 1, current_location[1])
    neighbors = []
    if direction == "up":
        if direction_count < straight_line_distance_max:
            neighbors.append((up_location, "up", direction_count + 1))
        neighbors.append((right_location, "right", 1))
        neighbors.append((left_location, "left", 1))
        
    elif direction == "down":
        if direction_count < straight_line_distance_max:
            neighbors.append((down_location, "down", direction_count + 1))
        neighbors.append((right_location, "right", 1))
        neighbors.append((left_location, "left", 1))
        
    elif direction == "left":
        if direction_count < straight_line_distance_max:
            neighbors.append((left_location, "left", direction_count + 1))
        neighbors.append((down_location, "down", 1))
        neighbors.append((up_location, "up", 1))
        
    elif direction == "right":
        if direction_count < straight_line_distance_max:
            neighbors.append((right_location, "right", direction_count + 1))
        neighbors.append((down_location, "down", 1))
        neighbors.append((up_location, "up", 1))
        
    elif direction == "start":
        neighbors.append((down_location, "down", 1))
        neighbors.append((right_location, "right", 1))
    
    for n in neighbors:
        step, direction, direction_count = n
        if inbounds(pattern, step):
            add_location_to_queue(priority, current_location, step, pattern[step[0]][step[1]], direction, direction_count)
    
    priority.task_done()
    
print(f"The least heat loss incurred is {distances[target]}")