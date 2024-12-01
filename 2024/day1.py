# read file into x y
x = []
y = []
with open("day1sample.txt", "r") as fp:
    for line in fp.readlines():
        clean = line.strip().split()
        x.append(int(clean[0]))
        y.append(int(clean[1]))

print(x)
print(y)

# sort x, y
x = sorted(x)
y = sorted(y)

print(x)
print(y)

# calculate sum(|x - y|)
ans = 0
for i in range(len(x)):
    ans = ans + abs(x[i] - y[i])

# print the ans
print(ans)

similarity = 0
for i, a in enumerate(x):
    cardinality = 0
    for j, b in enumerate(y):
        if a == b:
            cardinality += 1
    
    similarity += a * cardinality
    
print(similarity)