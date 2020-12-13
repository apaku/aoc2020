import sys

lines = sys.stdin.readlines()

if len(lines) == 2:
    target_time = int(lines[0].strip())
    busses = lines[1].split(",")

    busses_part1 = [int(x) for x in busses if x != 'x']

    wait_time = sorted(map(lambda bus: (bus - (target_time - ((target_time // bus) * bus)), bus), busses_part1))

    next_bus = wait_time[0]
    print("Part1 smallest_wait: {} product: {}".format(next_bus, next_bus[0] * next_bus[1]))

else:
    busses = lines[0].split(",")

busses_part2 = list(reversed(sorted(filter(lambda x: x[1] != 0, enumerate(map(lambda b: 0 if b == 'x' else int(b), busses))), key=lambda b: b[1])))
print("Part2: {}".format(busses_part2))
multiple = 1
while True:
    t = multiple * busses_part2[0][1] - busses_part2[0][0]
    nonmatching = False
    for bus in busses_part2[1:]:
        if ( t + bus[0] ) % bus[1] != 0:
            nonmatching = True
            break
    if not nonmatching:
        print("Part2: {}".format(t))
        break
    multiple += 1
