import re
import sys
import collections
rx = re.compile(r"(\d+)-(\d+) (\w): (.*)")
def parse(line):
    match = rx.match(line)
    return (int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))

validpws = []
lines = list(sys.stdin.readlines())
for pw in [parse(line.strip()) for line in lines]:
    count = pw[3].count(pw[2])
    if count >= pw[0] and count <= pw[1]:
        validpws.append(pw)

print("Part1: {}".format(len(validpws)))

validpws.clear()
for pw in [parse(line.strip()) for line in lines]:
    ch = pw[2]
    pwstr = pw[3]
    idx1 = pw[0]
    idx2 = pw[1]
    if (pwstr[idx1-1] == ch and pwstr[idx2-1] != ch) or (pwstr[idx1-1] != ch and pwstr[idx2-1] == ch):
        validpws.append(pw)

print("Part2: {}".format(len(validpws)))
