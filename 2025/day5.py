from dataclasses import dataclass

@dataclass
class ItemRange:
    low: int
    high: int
    
    def in_range(self, item: int) -> bool:
        return self.low <= item <= self.high
    
    def difference(self) -> int:
        return self.high - self.low + 1

ranges = []
spoiled_item_count = 0

with open("./2025/day5.txt", "r") as fp:
    line = fp.readline().strip()
    while line:
        low, high = line.split("-")
        ranges.append(ItemRange(int(low), int(high)))
        line = fp.readline().strip()
    
    line = fp.readline().strip()
    while line:
        for r in ranges:
            if r.in_range(int(line)):
                spoiled_item_count += 1
                break
        line = fp.readline().strip()
        
print(spoiled_item_count)


# use the ranges to determine how many ingredients can be fresh

# sort the ranges
ranges.sort(key=lambda r: r.low)

# track the range with the highest high value
# once we hit a new high value
# calculate an overlap
# add the ranges difference minus the overlap to the total
fresh_item_count = ranges[0].difference()
max_range = ranges[0]
for i, r in enumerate(ranges[1:]):
    if max_range.high >= r.high:
        continue
    
    if max_range.high >= r.low:
        overlap = max_range.high - r.low + 1
    else:
        overlap = 0
    fresh_item_count += r.difference() - overlap 
    max_range = r

print(fresh_item_count)