from functools import cache

@cache
def dfs(server, has_dac, has_fft):
    connections = graph[server]
    path_count = 0
    for c in connections:
        if c == "out":
            if has_dac and has_fft:
                return 1
            else:
                return 0
        else:
            new_has_dac = has_dac or c == "dac"
            new_has_fft = has_fft or c == "fft"
            path_count += dfs(c, new_has_dac, new_has_fft)
    return path_count

graph = {}
with open("./2025/day11.txt", "r") as fp:
    for line in fp.readlines():
        parts = line.strip().split(" ")
        key = parts[0][:-1] # take off the ':' character
        connections = parts[1:]
        graph[key] = connections
        
print(dfs("svr", False, False))