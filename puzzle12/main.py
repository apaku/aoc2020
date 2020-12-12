import sys
import itertools
import math

direction = 'E'
pos = (0,0)
right_rotation_helper = itertools.cycle(['E', 'S', 'W', 'N'])
left_rotation_helper = itertools.cycle(['E', 'N', 'W', 'S'])
instructions = [line.strip() for line in sys.stdin.readlines()]
for instr in instructions:
    if instr[0] == 'F':
        instr = direction + instr[1:]
    if instr[0] == 'E':
        pos = (pos[0]+int(instr[1:]), pos[1])
    elif instr[0] == 'W':
        pos = (pos[0]-int(instr[1:]), pos[1])
    elif instr[0] == 'N':
        pos = (pos[0], pos[1]-int(instr[1:]))
    elif instr[0] == 'S':
        pos = (pos[0], pos[1]+int(instr[1:]))
    elif instr[0] == 'R' or instr[0] == 'L':
        helper = right_rotation_helper if instr[0] == 'R' else left_rotation_helper
        rotation = int(instr[1:]) / 90
        while next(helper) != direction:
            pass
        while rotation > 0:
            direction = next(helper)
            rotation -= 1
    else:
        print("ERROR: {}".format(line))

    print("Moved to: {}".format(pos))
print("Part1: {}".format(abs(pos[0])+abs(pos[1])))

ship = (0,0)
waypoint = (10,-1)
for instr in instructions:
    if instr[0] == 'F':
        ship = (ship[0] + int(instr[1:]) * waypoint[0], ship[1] + int(instr[1:]) * waypoint[1])
    elif instr[0] == 'N':
        waypoint = (waypoint[0], waypoint[1] - int(instr[1:]))
    elif instr[0] == 'S':
        waypoint = (waypoint[0], waypoint[1] + int(instr[1:]))
    elif instr[0] == 'E':
        waypoint = (waypoint[0] + int(instr[1:]), waypoint[1])
    elif instr[0] == 'W':
        waypoint = (waypoint[0] - int(instr[1:]), waypoint[1])
    elif instr[0] == 'R' or instr[0] == 'L':
        theta = math.radians(int(instr[1:]))
        if instr[0] == 'R':
            theta = -theta
        x = round(waypoint[0] * math.cos(theta) + waypoint[1] * math.sin(theta))
        y = round(-waypoint[0] * math.sin(theta) + waypoint[1] * math.cos(theta))
        print("Rotating {} with {} to {}".format(waypoint, instr, (x,y)))
        waypoint = (int(x),int(y))
    else:
        print("ERROR: {}".format(instr))
    print("Moved with {} to {} {}".format(instr, ship, waypoint))
print("Part2: {}".format(abs(ship[0]) + abs(ship[1])))
