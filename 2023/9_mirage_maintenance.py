
data: list[list[int]] = []
with open('./day9.txt', 'r') as fp:
    for line in fp.readlines():
        data.append([int(x) for x in line.strip().split(" ")])


def nextSequence(seq: list[int]) -> int:
    # stop condition
    if set(seq) == {0}:
        return 0
    
    # reduce the list to the differences of elements
    dif: list[int] = []
    for i, _ in enumerate(seq):
        if i + 1 < len(seq):
            dif.append(seq[i+1] - seq[i])
    
    return seq[0] - nextSequence(dif)
        

# find the next value in each sequence 
sum_next_values = 0
for s in data:
    next = nextSequence(s)
    #print(f"{s} -> {next}")
    sum_next_values += next

print(sum_next_values)