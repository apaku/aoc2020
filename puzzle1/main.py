from itertools import combinations
import sys
data = [int(l.strip()) for l in sys.stdin.readlines()]

print("Input: {}".format(data))
entries = [(x,y) for x,y in combinations(data, 2) if x + y == 2020]

print("Entries: {}".format(list(entries)))

(a,b) = entries[0]
print("Result Part one: {}".format(a*b))

entries = [(x,y,z) for x,y,z in combinations(data, 3) if x + y + z == 2020]

print("Entries: {}".format(list(entries)))

(a,b,c) = entries[0]
print("Result Part one: {}".format(a*b*c))
