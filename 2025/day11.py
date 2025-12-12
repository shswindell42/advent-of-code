
graph = {}
with open("./2025/day11.txt", "r") as fp:
    for line in fp.readlines():
        parts = line.strip().split(" ")
        key = parts[0][:-1] # take off the ':' character
        connections = parts[1:]
        graph[key] = connections
        
visited_servers = set()
servers = ["you"]
path_count = 0
while servers:
    server = servers.pop()
    
    connections = graph[server]
    for c in connections:
        if c == "out":
            path_count += 1
        else:
            servers.append(c)

print(path_count)