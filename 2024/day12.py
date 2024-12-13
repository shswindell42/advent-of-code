directions = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
]

garden = [l.strip() for l in open("./2024/day12.txt").readlines()]
garden_regions = {}
region_side_counts = {}
visited = []

for y, r in enumerate(garden):
    for x, c in enumerate(r):
        if (x, y) not in visited:
            region_queue = [(x, y)]
            
            sides = []
            while len(region_queue) > 0:
                current_plot = region_queue.pop(0)
                
                if current_plot not in visited:
                    visited.append(current_plot)
                    
                    # calculate the perimeter, queue neighbors of the same crop
                    perimeter = 0
                    for d_i, d in enumerate(directions):
                        neighbor_coords = (current_plot[0] + d[0], current_plot[1] + d[1])
                        if 0 <= neighbor_coords[0] < len(r) and 0 <= neighbor_coords[1] < len(garden):
                            neighbor = garden[neighbor_coords[1]][neighbor_coords[0]]
                            if neighbor != c:
                                perimeter += 1
                                sides.append((current_plot, d_i))
                            else:
                                if neighbor_coords not in visited:
                                    region_queue.append(neighbor_coords)
                        else:
                            perimeter += 1
                            sides.append((current_plot, d_i))
                    
                    # accumulate the area and perimeter of the region
                    region_stats = garden_regions.get((x, y))
                    if region_stats:
                        new_stats = (region_stats[0] + 1, region_stats[1] + perimeter)
                        garden_regions[(x, y)] = new_stats
                    else:
                        garden_regions[(x, y)] = (1, perimeter)
                        
            # calc number of sides
            edges = {}
            for s in sides:
                direction_edges = edges.get(s[1])
                if direction_edges:
                    edges[s[1]].append(s[0])
                else:
                    edges[s[1]] = [s[0]]
            
            side_count = 0
            for d_i in edges.keys():
                side_count += 1
                edge_direction = 0 if d_i < 2 else 1
                edge_lock = 1 if d_i < 2 else 0
                edges[d_i].sort(key=lambda edge: (edge[edge_lock], edge[edge_direction]))
                for i in range(len(edges[d_i])):
                    # find contiguous edges that make a side
                    if i+1 < len(edges[d_i]):
                        e = edges[d_i][i]
                        next_e = edges[d_i][i+1]
                        if abs(e[edge_direction] - next_e[edge_direction]) != 1 or e[edge_lock] != next_e[edge_lock]:
                            side_count += 1
                    
            region_side_counts[(x, y)] = side_count
            
total_price = 0
for k, region in garden_regions.items():
    area = region[0]
    perimeter = region[1]
    sides = region_side_counts[k]
    total_price += area * sides
        
print(total_price)