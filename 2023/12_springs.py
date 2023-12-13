
from functools import cache

# determines if the spring can be satisifed by the group
def satisfy(spring: str, groups: list[int]) -> bool:
    return groups == [len(s) for s in spring.split(".") if s]

@cache
def numpos(spring, groups, curlen):
    if not spring:
        return not groups and curlen == 0 or len(groups) == 1 and groups[0] == curlen
    
    if groups and curlen > groups[0] or not groups and curlen:
        return 0
    
    total = 0
    if spring[0] in '#?':
        total += numpos(spring[1:], groups, curlen + 1)

    if spring[0] in '.?':
        if not curlen:
            total += numpos(spring[1:], groups, 0)
        elif curlen == groups[0]:
            total += numpos(spring[1:], groups[1:], 0)
    
    return total



sum_arrangements = 0
with open('./day12.txt', 'r') as fp:
    for line in fp.readlines():
        data = line.strip().split(' ')
        spring = ((data[0] + '?') * 5)[:-1]
        groups = tuple(map(int, data[1].split(','))) * 5

        sum_arrangements += numpos(spring, groups, 0)

        # possibilities = [spring]
        # stop = False
        # while not stop:
        #     stop = True
        #     if '?' in possibilities[0]:
        #         p = possibilities.pop(0)
        #         for i, c in enumerate(p):
        #             if c == '?':
        #                 p1 = p[:i] + '.' + p[i+1:]
        #                 possibilities.append(p1)
        #                 p2 = p[:i] + '#' + p[i+1:]
        #                 possibilities.append(p2)
        #                 stop = False
        #                 break

        # arrangements = [s for s in possibilities if satisfy(s, groups)]
        # sum_arrangements += len(arrangements)
        
print(sum_arrangements)