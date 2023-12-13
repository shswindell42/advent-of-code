import sys
from dataclasses import dataclass

@dataclass
class AlmanacEntry:
    destinationStart: int
    sourceStart: int
    rangeLength: int


almanacMaps: list[list[AlmanacEntry]] = []

with open("./day5.txt", 'r') as fp:
    seedLine = fp.readline()
    seeds = [int(x) for x in seedLine.split(":")[1].strip().split(" ")]

    # skip the first blank line
    fp.readline()

    currentAlmanac: list[AlmanacEntry] = []
    for line in fp.readlines():
        line = line.strip()
        if not line:
            almanacMaps.append(currentAlmanac)
            currentAlmanac = []
        elif "map" in line:
            pass
        else:
            # process the line into the currentAlmanac
            destination, source, length = [int(x) for x in line.split(" ")]
            entry = AlmanacEntry(destinationStart=destination, sourceStart=source, rangeLength=length)
            currentAlmanac.append(entry)

    # need to add the last currentAlmanac into almanacMaps
    almanacMaps.append(currentAlmanac)

seedPairs = [(s, seeds[i+1]) for i, s in enumerate(seeds) if i % 2 == 0]

minLocation = sys.maxsize
for seedStart, length in seedPairs:
    for seed in range(seedStart, seedStart + length):
        mappedValue = seed
        for map in almanacMaps:
            for entry in map:
                # am I in the entry?
                sourceEnd = entry.sourceStart + entry.rangeLength
                if mappedValue >= entry.sourceStart and mappedValue < sourceEnd:
                    offset = mappedValue - entry.sourceStart
                    mappedValue = entry.destinationStart + offset
                    break
    
        minLocation = min(minLocation, mappedValue)

print(minLocation)