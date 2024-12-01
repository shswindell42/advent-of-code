from copy import deepcopy
from queue import PriorityQueue
import math

class PatternWalk:
    def __init__(self):
        self.path: list[tuple[int,int]] = []
        self.priority: int = 0
        self.direction: str = "start"
        self.direction_count: int = 1
    
    def append(self, step: tuple[int, int], weight: int, direction: str):
        self.path.append(step)
        self.priority += weight
        
        if self.direction == direction:
            self.direction_count += 1
        else:
            self.direction = direction
            self.direction_count = 1
            
    def __lt__(self, other):
        return self.priority < other.priority


def inbounds(space: list[list[int]], location: tuple[int, int]) -> bool:
    return location[0] >= 0 and location[0] < len(space) and location[1] >= 0 and location[1] < len(space[0])

def add_location_to_queue(queue: PriorityQueue, path: PatternWalk, step: tuple[int, int], weight: int, direction: str) -> None:
    visited_node = [x for x in visited_nodes if x[0] == step[0] and x[1] == step[1] and x[2] == direction]
    
    add_to_queue = True if not visited_node else False
    
    if visited_node:
        old_node = visited_node[0]
        if old_node[3] > weight:
            visited_nodes.remove(old_node)
            add_to_queue = True
        
    if add_to_queue:
        new_path = deepcopy(path)
        new_path.append(step, weight, direction)
        queue.put(new_path)
        visited_nodes.append((*step, direction, weight))
    

with open('./day17sample.txt', 'r') as fp:
    pattern: list[list[int]] = []
    for l in fp.readlines():
        pattern.append(list([int(c) for c in l.strip()]))

end_location = (len(pattern) - 1, len(pattern[0]) - 1)
straight_line_distance_max = 3
# this list will act as the queue
possible_paths: PriorityQueue = PriorityQueue()
visited_nodes: list[tuple[int,int, str, int]] = []

start_path = PatternWalk()
start_path.append((0,0), 0, "start")

possible_paths.put(start_path)

while not possible_paths.empty():
    
    # take the first from the queue
    current_path = possible_paths.get()
    current_location = (current_path.path[-1][0], current_path.path[-1][1])

    # are we at the end?
    if current_location == end_location:
        break

    # evaluate the possible options and insert new PatternWalk objects into the queue
    right_location = (current_location[0], current_location[1] + 1)
    left_location = (current_location[0], current_location[1] - 1)
    up_location = (current_location[0] - 1, current_location[1])
    down_location = (current_location[0] + 1, current_location[1])
    
    if current_path.direction == "up":
        if inbounds(pattern, right_location):
            add_location_to_queue(possible_paths, current_path, right_location, pattern[right_location[0]][right_location[1]], "right")
        if inbounds(pattern, left_location):
            add_location_to_queue(possible_paths, current_path, left_location, pattern[left_location[0]][left_location[1]], "left")
        if current_path.direction_count < straight_line_distance_max:
            if inbounds(pattern, up_location):
                add_location_to_queue(possible_paths, current_path, up_location, pattern[up_location[0]][up_location[1]],"up")
    elif current_path.direction == "down":
        if inbounds(pattern, right_location):
            add_location_to_queue(possible_paths, current_path, right_location, pattern[right_location[0]][right_location[1]], "right")
        if inbounds(pattern, left_location):
            add_location_to_queue(possible_paths, current_path, left_location, pattern[left_location[0]][left_location[1]], "left")
        if current_path.direction_count < straight_line_distance_max:
            if inbounds(pattern, down_location):
                add_location_to_queue(possible_paths, current_path, down_location, pattern[down_location[0]][down_location[1]],"down")
    elif current_path.direction == "left":
        if inbounds(pattern, down_location):
            add_location_to_queue(possible_paths, current_path, down_location, pattern[down_location[0]][down_location[1]],"down")
        if inbounds(pattern, up_location):
            add_location_to_queue(possible_paths, current_path, up_location, pattern[up_location[0]][up_location[1]],"up")
        if current_path.direction_count < straight_line_distance_max:
            if inbounds(pattern, left_location):
                add_location_to_queue(possible_paths, current_path, left_location, pattern[left_location[0]][left_location[1]],"left")
    elif current_path.direction == "right":
        if inbounds(pattern, down_location):
            add_location_to_queue(possible_paths, current_path, down_location, pattern[down_location[0]][down_location[1]],"down")
        if inbounds(pattern, up_location):
            add_location_to_queue(possible_paths, current_path, up_location, pattern[up_location[0]][up_location[1]],"up")
        if current_path.direction_count < straight_line_distance_max:
            if inbounds(pattern, right_location):
                add_location_to_queue(possible_paths, current_path, right_location, pattern[right_location[0]][right_location[1]],"right")
    elif current_path.direction == "start":
        add_location_to_queue(possible_paths, current_path, right_location, pattern[right_location[0]][right_location[1]], "right")
        add_location_to_queue(possible_paths, current_path, down_location, pattern[down_location[0]][down_location[1]], "down")
        
    possible_paths.task_done()


print()
print(f"Weight is {current_path.priority}")
for i, r in enumerate(pattern):
    for j, c in enumerate(r):
        if (i, j, "up") in current_path.path:
            print("^", end="")
        elif (i, j, "down") in current_path.path:
            print("v", end="")
        elif (i, j, "left") in current_path.path:
            print("<", end="")
        elif (i, j, "right") in current_path.path:
            print(">", end="")
        else:
            print(c, end="")
    print()
    
    
print(f"The least heat loss incurred is {current_path.priority}")