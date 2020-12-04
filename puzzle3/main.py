
import sys

def parseLine(line):
    trees = []
    for i,c in enumerate(line):
        if c == '#':
            trees.append(i)
    return trees

def parse(lines):
    area = []
    for line in lines:
        linelen = len(line.strip())
        area.append(parseLine(line.strip()))
        print("trees in line: {}".format(area[-1]))
    return (linelen, area)

def hasTree(area, linelen, pos):
    print("Point:{} {}".format(pos.x, pos.y))
    line = area[pos.y]
    xpos = pos.x % linelen
    print("Checking line: {} at {}".format(line, xpos))
    if xpos in line:
        print("hit tree")
        return 1
    print("no tree")
    return 0

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def countTrees(area, linelen, walk):
    pos = point(0,0)
    numTrees = 0
    while pos.y < len(area):
        numTrees += hasTree(area, linelen, pos)
        pos.x += walk[0]
        pos.y += walk[1]
    return numTrees

(linelen, area) = parse([line.strip() for line in sys.stdin.readlines()])
print("LineLenght: {}".format(linelen))
product = 1
for walk in [(1,1), (3,1), (5,1), (7, 1), (1,2)]:
    count = countTrees(area, linelen, walk)
    print("number of trees hit: {}".format(count))
    product *= count
print("Product: {}".format(product))
