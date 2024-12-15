from functools import reduce 
from math import lcm

MAP_WIDTH = 101
MAP_HEIGHT = 103
SECONDS = 100

mid_width = MAP_WIDTH // 2
mid_height = MAP_HEIGHT // 2    

quad_map = {
    (False, False): 0,
    (True, False): 1,
    (False, True): 2,
    (True, True): 3
}

quad_count = [0, 0, 0, 0]

def move_robot(r, t):
    p, v = r
    p_x = (p[0] + (v[0] * t)) % MAP_WIDTH
    p_y = (p[1] + (v[1] * t)) % MAP_HEIGHT
    return ((p_x, p_y), v)
    
moved_robots = []
robots = []
with open("./2024/day14.txt") as f:
    for line in f:
        p, v = line.strip().split(" ")
        p_x, p_y = p.split('=')[1].split(',')
        v_x, v_y = v.split('=')[1].split(',')
        robot = ((int(p_x), int(p_y)), (int(v_x), int(v_y)))
        robots.append(robot)
        robot_moved = move_robot(robot, SECONDS)

        pos = robot_moved[0]
        if pos[0] != mid_width and pos[1] != mid_height:
            width_flag = pos[0] > mid_width
            height_flag = pos[1] > mid_height
            quad_count[quad_map[(width_flag, height_flag)]] += 1

safety_factor = reduce(lambda product, x: product * x, quad_count)
print(safety_factor)

def print_robots(robots):
    points = [r[0] for r in robots]
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if (x, y) in points:
                print("X", end="")
            else:
                print(".", end="")
        print("")

# step = MAP_HEIGHT
# for i in range(10):
#     robots = [move_robot(r, step) for r in robots]
#     print(f"Iteration {(i) * step}")
#     print_robots(robots)
#     print("")
#     time.sleep(1)
#     os.system("clear")

#print_robots(robots)
# print(lcm(MAP_WIDTH, MAP_HEIGHT))
# step = lcm(MAP_WIDTH, MAP_HEIGHT)
robots = [move_robot(r, 7569) for r in robots]
print_robots(robots)


# 95 - y grouping repeats
# 50 - x grouping repeats
step = 1
max_iteration = 0
max_robot_count = 0
for i in range(6000,10000):
    if i % 1000 == 0:
        print(max_iteration)
    robots = [move_robot(r, step) for r in robots]

    points = [r[0] for r in robots]
    for y in range(MAP_HEIGHT):
        robot_count = 0
        for x in range(MAP_WIDTH):
            if (x, y) in points:
                robot_count += 1
        
        if robot_count > max_robot_count:
            max_robot_count = robot_count
            max_iteration = i+1
                
print(max_iteration)