import sys
from collections import defaultdict
from queue import PriorityQueue

max_momentum = 10
min_momentum = 4

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

opposite_directions = {
    "up": "down",
    "down": "up",
    "left": "right", 
    "right": "left",
    "none": "none"
}
    
    
def read_map_file(file: str) -> list[list[int]]:
    with open(file, 'r') as fp:
        map: list[list[int]] = []
        for l in fp.readlines():
            map.append(list([int(c) for c in l.strip()]))
    
    return map

def init_distance_map(init_node: tuple[int,int,int,str,int]) -> defaultdict:
    distance = defaultdict(lambda: sys.maxsize)
        
    distance[(0,0,0,"none",0)] = 0 # start node is 0
    return distance

# def init_queue(map: list[list[int]]) -> list[tuple[int, int, int, str]]:
#     directions = ['up', 'down', 'left', 'right']
#     queue = []
#     for y in range(len(map)):
#         for x in range(len(map[0])):
#             for m in range(1,4):
#                 for d in directions:
#                     queue.append((y, x, m, d))
    
#     return queue

def print_map(map: list[list[int]]) -> None:
    for r in map:
        for c in r:
            if c != sys.maxsize:
                print(c, end="")
            else:
                print("_", end="")
        print()


def is_inbounds(map: list[list[int]], row: int, col: int) -> bool:
    return 0 <= row < len(map) and 0 <= col < len(map[0])

def get_neighbors(map: list[list[int]], row: int, col: int, momentum: int, direction: str) -> list[tuple[int, int, int, str, int]]:
    neighbors: list[tuple[int, int, int]] = []
    
    for d in directions:
        if (d == direction and min_momentum > momentum) or direction == "none" or (opposite_directions[direction] != d and (min_momentum <= momentum and direction != d)):
            next_cord = (row + directions[d][0], col + directions[d][1])
            check_cord = (row + directions[d][0] * (min_momentum), col + directions[d][1] * (min_momentum))
            if is_inbounds(map, check_cord[0], check_cord[1]):
                neighbor = (
                        check_cord[0], 
                        check_cord[1], 
                        min_momentum,
                        d,
                        max(
                            sum([y for x in map[next_cord[0]:check_cord[0] + 1] for y in x[next_cord[1]:check_cord[1] + 1]])
                            ,sum([y for x in map[check_cord[0]:next_cord[0] + 1] for y in x[check_cord[1]:next_cord[1] + 1]])
                        )
                    )
                
                neighbors.append(neighbor)
        elif momentum < max_momentum and direction == d:
            check_cord = (row + directions[d][0], col + directions[d][1])
            if is_inbounds(map, check_cord[0], check_cord[1]):
                neighbor = (
                        check_cord[0], 
                        check_cord[1], 
                        1 if direction != d else momentum + 1,
                        d,
                        map[check_cord[0]][check_cord[1]]
                    )
                
                neighbors.append(neighbor)
                    
    return neighbors
    
def solve(file: str) -> int:
    map = read_map_file(file)
    
    # initialize distance map
    start_node = (0, (0,0,0,"none",0))
    distance = init_distance_map(start_node)
    
    # initialize visited list
    visited_nodes = []
    
    
    #queue = init_queue(map)
    queue = PriorityQueue()
    queue.put(start_node) # initialize with the start node
    
    # run dijkstra's algo
    while not queue.empty():
        #queue.sort(key=lambda n: distance[n])
        node = queue.get()[1]
        visited_nodes.append(node)
        
        if node[0] == len(map) - 1 and node[1] == len(map[0]) - 1:
            return distance[node]
        
        neighbors = get_neighbors(map, node[0], node[1], node[2], node[3])
        
        for n in neighbors:
            if distance[n] > distance[node] + n[4]:
                distance[n] = distance[node] + n[4]
                if n not in visited_nodes:
                    queue.put((distance[n], n))
        #print_map(distance_map)
    
    return -1
    
if __name__ == "__main__":
    print(solve('./day17.txt'))
    
    # print(solve('./day17_test2.txt'))
    # print(solve('./day17sample.txt'))
    
    # map = read_map_file('./day17_test2.txt')
    # neighbors = get_neighbors(map, 4, 8, 4, 'down')
    # for n in neighbors:
    #     print(n)
