import math

with open('./day6.txt', 'r') as fp:
    #times = [int(x) for x in fp.readline().split(":")[1].strip().split(" ") if x]
    #distances = [int(x) for x in fp.readline().split(":")[1].strip().split(" ") if x]
    times = [int(fp.readline().split(":")[1].strip().replace(" ", ""))]
    distances = [int(fp.readline().split(":")[1].strip().replace(" ", ""))]


magicNumber = 1
for t, d in zip(times, distances):
    a = -1
    b = t
    c = -1 * d

    ans1 = ((-1 * b) + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    ans2 = ((-1 * b) - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

    bottom = math.floor(ans1 + 1)
    top = math.ceil(ans2 - 1)

    possible = top - bottom + 1
    magicNumber *= possible

print(magicNumber)