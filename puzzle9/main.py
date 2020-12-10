import sys
from itertools import combinations

data = [int(line.strip()) for line in sys.stdin.readlines()]

preamble = int(sys.argv[1])

idx = preamble
while idx < len(data):
    found = False
    for (a,b) in combinations(data[idx-preamble:idx], 2):
        if a + b == data[idx]:
            found = True
            break
    if not found:
        break
    idx += 1

print("Part1: {} - {}".format(idx, data[idx]))

subdata = data[:idx]

subidx = 0
while subidx < len(subdata)-1:
    endidx = subidx + 1
    while endidx < len(subdata):
        sublist = subdata[subidx:endidx]
        if sum(sublist) == data[idx]:
            print("Part2: {} {}".format(sublist, min(sublist)+max(sublist)))
            sys.exit(0)
        endidx += 1
    subidx += 1
